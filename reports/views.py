from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from django.db.models import Sum, Count, Q, Avg
from django.utils import timezone
from datetime import datetime, timedelta, date
from decimal import Decimal

from hotel.models import Booking, Room, Payment, RoomType, Reservation
from userAccount.models import Profil
from .serializers import (
    UnifiedKPISerializer,
    PeriodFilterSerializer,
    DashboardSummarySerializer,
    ChartDataSerializer,
    RoomStatusChartSerializer
)


class UnifiedKPIView(APIView):
    """API unifiée pour les KPIs qui s'adapte selon le rôle de l'utilisateur"""
    
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        # Vérifier si l'utilisateur a les permissions nécessaires
        user_groups = request.user.groups.values_list('name', flat=True)
        
        if not any(group in ['admin', 'gérant'] for group in user_groups):
            return Response(
                {'error': 'Accès non autorisé. Seuls les admins et gérants peuvent accéder aux KPIs.'}, 
                status=status.HTTP_403_FORBIDDEN
            )
        
        # Déterminer le rôle principal de l'utilisateur
        if 'admin' in user_groups:
            user_role = 'admin'
        elif 'gérant' in user_groups:
            user_role = 'gerant'
        else:
            user_role = 'unknown'
        
        try:
            # Générer les données selon le rôle
            if user_role == 'admin':
                data = self._get_admin_kpis(request)
            else:  # gérant
                data = self._get_gerant_kpis(request)
            
            # Ajouter les méta-informations
            data['user_role'] = user_role
            data['date_derniere_mise_a_jour'] = timezone.now().isoformat()
            
            # Retourner directement les données sans validation stricte du serializer
            return Response(data, status=status.HTTP_200_OK)
            
        except Exception as e:
            return Response(
                {'error': f'Erreur lors du calcul des KPIs: {str(e)}'}, 
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
    
    def _get_admin_kpis(self, request):
        """Générer les KPIs pour les administrateurs avec filtrage par période"""
        
        period = request.query_params.get('period', 'today')
        
        # Calculer les dates selon la période
        start_date, end_date = self._get_period_dates(period)
        start_date_prev, end_date_prev = self._get_previous_period_dates(period, start_date, end_date)
        
        # Calculer les KPIs pour la période actuelle
        current_data = self._calculate_admin_kpis(start_date, end_date)
        
        # Calculer les KPIs pour la période précédente
        previous_data = self._calculate_admin_kpis(start_date_prev, end_date_prev)
        
        # Calculer les évolutions
        evolution_data = self._calculate_evolution(current_data, previous_data)
        
        # Préparer la réponse admin
        response_data = {
            'period': period,
            'periode_debut': start_date.isoformat(),
            'periode_fin': end_date.isoformat(),
        }
        
        # Ajouter les données actuelles
        response_data.update(current_data)
        
        # Ajouter les données précédentes avec le suffixe '_precedent'
        for key, value in previous_data.items():
            response_data[f"{key}_precedent"] = value
        
        # Ajouter les évolutions
        response_data.update(evolution_data)
        
        return response_data
    
    def _get_gerant_kpis(self, request):
        """Générer les KPIs pour les gérants (données du jour)"""
        
        today = timezone.now().date()
        start_of_day = datetime.combine(today, datetime.min.time())
        end_of_day = datetime.combine(today, datetime.max.time())
        
        start_of_day = timezone.make_aware(start_of_day)
        end_of_day = timezone.make_aware(end_of_day)
        
        # Revenus du jour
        revenus_jour = Payment.objects.filter(
            created_at__range=[start_of_day, end_of_day]
        ).aggregate(total=Sum('amount'))['total'] or Decimal('0')
        
        # Locations actives
        locations_actives = Booking.objects.filter(
            status='ongoing',
            checkIn__lte=end_of_day,
            checkOut__gte=start_of_day
        ).count()
        
        # Entrées prévues aujourd'hui
        entrees_today = Booking.objects.filter(
            checkIn__date=today,
            status='ongoing'
        )
        entrees_prevues = entrees_today.count()
        
        # Détails des entrées
        entrees_details = []
        for booking in entrees_today:
            entrees_details.append({
                'reference': booking.reference,
                'client': f"{booking.guest.name} {booking.guest.firstname}",
                'chambre': booking.room.number,
                'heure_arrivee': booking.checkIn.strftime('%H:%M'),
                'montant': float(booking.totalPrice)
            })
        
        # Sorties prévues aujourd'hui
        sorties_today = Booking.objects.filter(
            checkOut__date=today,
            status='ongoing'
        )
        sorties_prevues = sorties_today.count()
        
        # Détails des sorties
        sorties_details = []
        for booking in sorties_today:
            sorties_details.append({
                'reference': booking.reference,
                'client': f"{booking.guest.name} {booking.guest.firstname}",
                'chambre': booking.room.number,
                'heure_depart': booking.checkOut.strftime('%H:%M'),
                'montant_paye': float(booking.amountPaid),
                'montant_du': float(booking.amountDue)
            })
        
        return {
            'revenus_jour': str(revenus_jour),
            'locations_actives': locations_actives,
            'entrees_prevues': entrees_prevues,
            'sorties_prevues': sorties_prevues,
            'entrees_details': entrees_details,
            'sorties_details': sorties_details,
            'date_du_jour': today.isoformat()
        }
    
    def _get_period_dates(self, period):
        """Calculer les dates de début et fin selon la période"""
        now = timezone.now()
        today = now.date()
        
        if period == 'today':
            start_date = datetime.combine(today, datetime.min.time())
            end_date = datetime.combine(today, datetime.max.time())
        
        elif period == 'week':
            # Semaine actuelle (lundi à dimanche)
            start_date = datetime.combine(today - timedelta(days=today.weekday()), datetime.min.time())
            end_date = datetime.combine(start_date.date() + timedelta(days=6), datetime.max.time())
        
        elif period == 'month':
            # Mois actuel
            start_date = datetime.combine(today.replace(day=1), datetime.min.time())
            if today.month == 12:
                next_month = today.replace(year=today.year + 1, month=1, day=1)
            else:
                next_month = today.replace(month=today.month + 1, day=1)
            end_date = datetime.combine(next_month - timedelta(days=1), datetime.max.time())
        
        elif period == 'quarter':
            # Trimestre actuel
            quarter = (today.month - 1) // 3 + 1
            start_month = (quarter - 1) * 3 + 1
            start_date = datetime.combine(today.replace(month=start_month, day=1), datetime.min.time())
            
            if quarter == 4:
                end_month_start = today.replace(year=today.year + 1, month=1, day=1)
            else:
                end_month_start = today.replace(month=start_month + 3, day=1)
            end_date = datetime.combine(end_month_start - timedelta(days=1), datetime.max.time())
        
        elif period == 'semester':
            # Semestre actuel
            if today.month <= 6:
                start_date = datetime.combine(today.replace(month=1, day=1), datetime.min.time())
                end_date = datetime.combine(today.replace(month=6, day=30), datetime.max.time())
            else:
                start_date = datetime.combine(today.replace(month=7, day=1), datetime.min.time())
                end_date = datetime.combine(today.replace(month=12, day=31), datetime.max.time())
        
        elif period == 'year':
            # Année actuelle
            start_date = datetime.combine(today.replace(month=1, day=1), datetime.min.time())
            end_date = datetime.combine(today.replace(month=12, day=31), datetime.max.time())
        
        else:
            # Par défaut, aujourd'hui
            start_date = datetime.combine(today, datetime.min.time())
            end_date = datetime.combine(today, datetime.max.time())
        
        return timezone.make_aware(start_date), timezone.make_aware(end_date)
    
    def _get_previous_period_dates(self, period, current_start, current_end):
        """Calculer les dates de la période précédente"""
        if period == 'today':
            prev_date = current_start.date() - timedelta(days=1)
            start_date = datetime.combine(prev_date, datetime.min.time())
            end_date = datetime.combine(prev_date, datetime.max.time())
        
        elif period == 'week':
            start_date = current_start - timedelta(days=7)
            end_date = current_end - timedelta(days=7)
        
        elif period == 'month':
            if current_start.month == 1:
                prev_month = current_start.replace(year=current_start.year - 1, month=12)
            else:
                prev_month = current_start.replace(month=current_start.month - 1)
            
            start_date = prev_month.replace(day=1)
            # Dernier jour du mois précédent
            if prev_month.month == 12:
                next_month = prev_month.replace(year=prev_month.year + 1, month=1, day=1)
            else:
                next_month = prev_month.replace(month=prev_month.month + 1, day=1)
            end_date = next_month - timedelta(days=1)
            end_date = datetime.combine(end_date.date(), datetime.max.time())
        
        elif period in ['quarter', 'semester', 'year']:
            # Calculer la durée de la période actuelle
            duration = current_end - current_start
            start_date = current_start - duration - timedelta(days=1)
            end_date = current_start - timedelta(days=1)
        
        else:
            # Par défaut
            duration = current_end - current_start
            start_date = current_start - duration
            end_date = current_end - duration
        
        return start_date, end_date
    
    def _calculate_admin_kpis(self, start_date, end_date):
        """Calculer les KPIs pour les administrateurs sur une période donnée"""
        
        # Filtrer les bookings dans la période
        payments = Payment.objects.filter(
            created_at__range=[start_date, end_date]
        )
        bookings = Booking.objects.filter(
            checkIn__range=[start_date, end_date]
        )
        
        # Calculer le revenu total (somme des montants payés)
        revenu_total = payments.aggregate(
            total=Sum('amount')
        )['total'] or Decimal('0')
        
        # Nombre total de locations
        nombre_locations = bookings.count()
        
        # Calculer le taux d'occupation
        total_rooms = Room.objects.count()
        if total_rooms > 0:
            # Bookings actifs pendant la période
            occupied_bookings = Booking.objects.filter(
                Q(checkIn__lte=end_date) & Q(checkOut__gte=start_date),
                status='ongoing'
            ).count()
            
            taux_occupation = (occupied_bookings / total_rooms) * 100
        else:
            taux_occupation = Decimal('0')
        
        # Calculer RevPAR (Revenue Per Available Room)
        if total_rooms > 0:
            revpar = revenu_total / total_rooms
        else:
            revpar = Decimal('0')
        
        return {
            'revenu_total': revenu_total,
            'taux_occupation': Decimal(str(taux_occupation)).quantize(Decimal('0.01')),
            'revpar': Decimal(str(revpar)).quantize(Decimal('0.01')),
            'nombre_locations': nombre_locations
        }
    
    def _calculate_evolution(self, current, previous):
        """Calculer l'évolution entre les périodes"""
        evolution = {}
        
        for key in ['revenu_total', 'taux_occupation', 'revpar', 'nombre_locations']:
            current_val = float(current.get(key, 0)) if isinstance(current.get(key), str) else current.get(key, 0)
            previous_val = float(previous.get(key, 0)) if isinstance(previous.get(key), str) else previous.get(key, 0)
            
            if previous_val > 0:
                evolution_pct = ((current_val - previous_val) / previous_val) * 100
            else:
                evolution_pct = 100 if current_val > 0 else 0
            
            evolution[f'evolution_{key.replace("_total", "")}'] = Decimal(str(evolution_pct)).quantize(Decimal('0.01'))
        
        return evolution


class DashboardSummaryView(APIView):
    """API pour le résumé global du dashboard"""
    
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        now = timezone.now()
        today = now.date()
        
        # Statistiques des chambres
        total_chambres = Room.objects.count()
        chambres_occupees = Room.objects.filter(
            status__in=['os', 'og', 'op']
        ).count()
        chambres_libres = Room.objects.filter(
            status__in=['lp']
        ).count()
        chambres_sale = Room.objects.filter(
            status__in=['ls', 'os']
        ).count()
        
        # Revenus par période
        start_today = datetime.combine(today, datetime.min.time())
        end_today = datetime.combine(today, datetime.max.time())
        start_month = datetime.combine(today.replace(day=1), datetime.min.time())
        start_year = datetime.combine(today.replace(month=1, day=1), datetime.min.time())
        
        start_today = timezone.make_aware(start_today)
        end_today = timezone.make_aware(end_today)
        start_month = timezone.make_aware(start_month)
        start_year = timezone.make_aware(start_year)
        
        revenus_today = Booking.objects.filter(
            created_at__range=[start_today, end_today]
        ).aggregate(total=Sum('amountPaid'))['total'] or Decimal('0')
        
        revenus_month = Booking.objects.filter(
            created_at__gte=start_month
        ).aggregate(total=Sum('amountPaid'))['total'] or Decimal('0')
        
        revenus_year = Booking.objects.filter(
            created_at__gte=start_year
        ).aggregate(total=Sum('amountPaid'))['total'] or Decimal('0')
        
        # Locations par période
        locations_today = Booking.objects.filter(
            created_at__range=[start_today, end_today]
        ).count()
        
        locations_month = Booking.objects.filter(
            created_at__gte=start_month
        ).count()
        
        locations_year = Booking.objects.filter(
            created_at__gte=start_year
        ).count()
        
        # Taux d'occupation
        if total_chambres > 0:
            taux_occupation_today = (chambres_occupees / total_chambres) * 100
            
            # Pour le mois et l'année, calculer la moyenne
            taux_occupation_month = taux_occupation_today  # Simplification
            taux_occupation_year = taux_occupation_today   # Simplification
        else:
            taux_occupation_today = taux_occupation_month = taux_occupation_year = 0
        
        data = {
            'total_chambres': total_chambres,
            'chambres_occupees': chambres_occupees,
            'chambres_libres': chambres_libres,
            'chambres_sale': chambres_sale,
            'revenus_today': revenus_today,
            'revenus_month': revenus_month,
            'revenus_year': revenus_year,
            'locations_today': locations_today,
            'locations_month': locations_month,
            'locations_year': locations_year,
            'taux_occupation_today': Decimal(str(taux_occupation_today)).quantize(Decimal('0.01')),
            'taux_occupation_month': Decimal(str(taux_occupation_month)).quantize(Decimal('0.01')),
            'taux_occupation_year': Decimal(str(taux_occupation_year)).quantize(Decimal('0.01')),
            'date_derniere_mise_a_jour': now.isoformat()
        }
        
        return Response(data, status=status.HTTP_200_OK)


class ChartDataView(APIView):
    """API pour les données de graphiques du dashboard"""
    
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        """Retourner les données pour les graphiques selon le type et la période"""
        
        # Récupérer les paramètres
        chart_type = request.query_params.get('type', 'revenus')
        period = request.query_params.get('period', 'day')
        
        # Valider les paramètres
        valid_chart_types = ['revenus', 'occupation', 'reservations']
        valid_periods = ['day', 'week', 'month', 'year']
        
        if chart_type not in valid_chart_types:
            return Response(
                {'error': f'Type de graphique invalide. Types valides: {valid_chart_types}'}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        
        if period not in valid_periods:
            return Response(
                {'error': f'Période invalide. Périodes valides: {valid_periods}'}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        
        try:
            # Générer les données selon le type et la période
            if chart_type == 'revenus':
                data = self._get_revenue_data(period)
            elif chart_type == 'occupation':
                data = self._get_occupation_data(period)
            elif chart_type == 'reservations':
                data = self._get_reservations_data(period)
            
            # Ajouter les méta-informations
            data.update({
                'chart_type': chart_type,
                'period': period,
                'generated_at': timezone.now().isoformat()
            })
            
            return Response(data, status=status.HTTP_200_OK)
            
        except Exception as e:
            return Response(
                {'error': f'Erreur lors de la génération des données: {str(e)}'}, 
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
    
    def _get_revenue_data(self, period):
        """Obtenir les données de revenus selon la période"""
        now = timezone.now()
        today = now.date()
        
        if period == 'day':
            # Données jour par jour pour la semaine courante
            start_of_week = today - timedelta(days=today.weekday())
            labels = []
            data = []
            
            for i in range(7):
                day = start_of_week + timedelta(days=i)
                day_name = self._get_day_name(day.weekday())
                labels.append(f"{day_name}\n{day.strftime('%d/%m')}")
                
                start_day = timezone.make_aware(datetime.combine(day, datetime.min.time()))
                end_day = timezone.make_aware(datetime.combine(day, datetime.max.time()))
                
                daily_revenue = Payment.objects.filter(
                    created_at__range=[start_day, end_day]
                ).aggregate(total=Sum('amount'))['total'] or 0
                
                data.append(daily_revenue)
            
            chart_title = "Revenus par jour"
            chart_subtitle = f"Semaine du {start_of_week.strftime('%d/%m/%Y')}"
            period_info = "Semaine courante"
            
        elif period == 'week':
            # Données semaine par semaine pour le mois courant
            start_of_month = today.replace(day=1)
            labels = []
            data = []
            
            current_week_start = start_of_month
            week_num = 1
            
            while current_week_start.month == today.month:
                week_end = min(current_week_start + timedelta(days=6), 
                              today.replace(month=today.month + 1 if today.month < 12 else 1, 
                                          year=today.year + 1 if today.month == 12 else today.year, 
                                          day=1) - timedelta(days=1))
                
                if week_end.month != today.month:
                    week_end = today.replace(day=1).replace(month=today.month + 1 if today.month < 12 else 1) - timedelta(days=1)
                
                labels.append(f"Semaine {week_num}\n{current_week_start.strftime('%d/%m')} - {week_end.strftime('%d/%m')}")
                
                start_week = timezone.make_aware(datetime.combine(current_week_start, datetime.min.time()))
                end_week = timezone.make_aware(datetime.combine(week_end, datetime.max.time()))
                
                weekly_revenue = Payment.objects.filter(
                    created_at__range=[start_week, end_week]
                ).aggregate(total=Sum('amount'))['total'] or 0
                
                data.append(weekly_revenue)
                
                current_week_start = week_end + timedelta(days=1)
                week_num += 1
                
                if current_week_start > today:
                    break
            
            chart_title = "Revenus par semaine"
            chart_subtitle = f"{self._get_month_name(today.month)} {today.year}"
            period_info = "Mois courant"
            
        elif period == 'month':
            # Données mois par mois pour l'année courante
            labels = []
            data = []
            
            for month in range(1, 13):
                month_name = self._get_month_name(month)
                labels.append(month_name)
                
                start_month = timezone.make_aware(datetime.combine(
                    today.replace(month=month, day=1), datetime.min.time()
                ))
                
                if month == 12:
                    end_month = timezone.make_aware(datetime.combine(
                        today.replace(year=today.year + 1, month=1, day=1) - timedelta(days=1), 
                        datetime.max.time()
                    ))
                else:
                    end_month = timezone.make_aware(datetime.combine(
                        today.replace(month=month + 1, day=1) - timedelta(days=1), 
                        datetime.max.time()
                    ))
                
                monthly_revenue = Payment.objects.filter(
                    created_at__range=[start_month, end_month]
                ).aggregate(total=Sum('amount'))['total'] or 0
                
                data.append(monthly_revenue)
            
            chart_title = "Revenus par mois"
            chart_subtitle = str(today.year)
            period_info = "Année courante"
            
        elif period == 'year':
            # Données des 5 dernières années
            labels = []
            data = []
            
            for i in range(4, -1, -1):  # De -4 à 0 (5 années)
                year = today.year - i
                labels.append(str(year))
                
                start_year = timezone.make_aware(datetime.combine(
                    date(year, 1, 1), datetime.min.time()
                ))
                end_year = timezone.make_aware(datetime.combine(
                    date(year, 12, 31), datetime.max.time()
                ))
                
                yearly_revenue = Payment.objects.filter(
                    created_at__range=[start_year, end_year]
                ).aggregate(total=Sum('amount'))['total'] or 0
                
                data.append(yearly_revenue)
            
            chart_title = "Revenus par année"
            chart_subtitle = f"{today.year - 4} - {today.year}"
            period_info = "5 dernières années"
        
        total = sum(data)
        
        return {
            'labels': labels,
            'data': data,
            'chart_title': chart_title,
            'chart_subtitle': chart_subtitle,
            'unit': 'FCFA',
            'period_info': period_info,
            'total': total
        }
    
    def _get_occupation_data(self, period):
        """Obtenir les données d'occupation (nombre de locations) selon la période"""
        now = timezone.now()
        today = now.date()
        
        if period == 'day':
            # Données jour par jour pour la semaine courante
            start_of_week = today - timedelta(days=today.weekday())
            labels = []
            data = []
            
            for i in range(7):
                day = start_of_week + timedelta(days=i)
                day_name = self._get_day_name(day.weekday())
                labels.append(f"{day_name}\n{day.strftime('%d/%m')}")
                
                start_day = timezone.make_aware(datetime.combine(day, datetime.min.time()))
                end_day = timezone.make_aware(datetime.combine(day, datetime.max.time()))
                
                daily_bookings = Booking.objects.filter(
                    checkIn__range=[start_day, end_day]
                ).count()
                
                data.append(daily_bookings)
                print(data)
            chart_title = "Locations par jour"
            chart_subtitle = f"Semaine du {start_of_week.strftime('%d/%m/%Y')}"
            period_info = "Semaine courante"
            
        elif period == 'week':
            # Données semaine par semaine pour le mois courant
            start_of_month = today.replace(day=1)
            labels = []
            data = []
            
            current_week_start = start_of_month
            week_num = 1
            
            while current_week_start.month == today.month:
                week_end = min(current_week_start + timedelta(days=6), 
                              today.replace(month=today.month + 1 if today.month < 12 else 1, 
                                          year=today.year + 1 if today.month == 12 else today.year, 
                                          day=1) - timedelta(days=1))
                
                if week_end.month != today.month:
                    week_end = today.replace(day=1).replace(month=today.month + 1 if today.month < 12 else 1) - timedelta(days=1)
                
                labels.append(f"Semaine {week_num}\n{current_week_start.strftime('%d/%m')} - {week_end.strftime('%d/%m')}")
                
                start_week = timezone.make_aware(datetime.combine(current_week_start, datetime.min.time()))
                end_week = timezone.make_aware(datetime.combine(week_end, datetime.max.time()))
                
                weekly_bookings = Booking.objects.filter(
                    created_at__range=[start_week, end_week]
                ).count()
                
                data.append(weekly_bookings)
                
                current_week_start = week_end + timedelta(days=1)
                week_num += 1
                
                if current_week_start > today:
                    break
            
            chart_title = "Locations par semaine"
            chart_subtitle = f"{self._get_month_name(today.month)} {today.year}"
            period_info = "Mois courant"
            
        elif period == 'month':
            # Données mois par mois pour l'année courante
            labels = []
            data = []
            
            for month in range(1, 13):
                month_name = self._get_month_name(month)
                labels.append(month_name)
                
                start_month = timezone.make_aware(datetime.combine(
                    today.replace(month=month, day=1), datetime.min.time()
                ))
                
                if month == 12:
                    end_month = timezone.make_aware(datetime.combine(
                        today.replace(year=today.year + 1, month=1, day=1) - timedelta(days=1), 
                        datetime.max.time()
                    ))
                else:
                    end_month = timezone.make_aware(datetime.combine(
                        today.replace(month=month + 1, day=1) - timedelta(days=1), 
                        datetime.max.time()
                    ))
                
                monthly_bookings = Booking.objects.filter(
                    created_at__range=[start_month, end_month]
                ).count()
                
                data.append(monthly_bookings)
            
            chart_title = "Locations par mois"
            chart_subtitle = str(today.year)
            period_info = "Année courante"
            
        elif period == 'year':
            # Données des 5 dernières années
            labels = []
            data = []
            
            for i in range(4, -1, -1):  # De -4 à 0 (5 années)
                year = today.year - i
                labels.append(str(year))
                
                start_year = timezone.make_aware(datetime.combine(
                    date(year, 1, 1), datetime.min.time()
                ))
                end_year = timezone.make_aware(datetime.combine(
                    date(year, 12, 31), datetime.max.time()
                ))
                
                yearly_bookings = Booking.objects.filter(
                    created_at__range=[start_year, end_year]
                ).count()
                
                data.append(yearly_bookings)
            
            chart_title = "Locations par année"
            chart_subtitle = f"{today.year - 4} - {today.year}"
            period_info = "5 dernières années"
        
        total = sum(data)
        
        return {
            'labels': labels,
            'data': data,
            'chart_title': chart_title,
            'chart_subtitle': chart_subtitle,
            'unit': 'nombre',
            'period_info': period_info,
            'total': total
        }
    
    def _get_reservations_data(self, period):
        """Obtenir les données de réservations selon la période"""
        now = timezone.now()
        today = now.date()
        
        if period == 'day':
            # Données jour par jour pour la semaine courante
            start_of_week = today - timedelta(days=today.weekday())
            labels = []
            data = []
            
            for i in range(7):
                day = start_of_week + timedelta(days=i)
                day_name = self._get_day_name(day.weekday())
                labels.append(f"{day_name}\n{day.strftime('%d/%m')}")
                
                start_day = timezone.make_aware(datetime.combine(day, datetime.min.time()))
                end_day = timezone.make_aware(datetime.combine(day, datetime.max.time()))
                
                daily_reservations = Reservation.objects.filter(
                    created_at__range=[start_day, end_day]
                ).count()
                
                data.append(daily_reservations)
            
            chart_title = "Réservations par jour"
            chart_subtitle = f"Semaine du {start_of_week.strftime('%d/%m/%Y')}"
            period_info = "Semaine courante"
            
        elif period == 'week':
            # Données semaine par semaine pour le mois courant
            start_of_month = today.replace(day=1)
            labels = []
            data = []
            
            current_week_start = start_of_month
            week_num = 1
            
            while current_week_start.month == today.month:
                week_end = min(current_week_start + timedelta(days=6), 
                              today.replace(month=today.month + 1 if today.month < 12 else 1, 
                                          year=today.year + 1 if today.month == 12 else today.year, 
                                          day=1) - timedelta(days=1))
                
                if week_end.month != today.month:
                    week_end = today.replace(day=1).replace(month=today.month + 1 if today.month < 12 else 1) - timedelta(days=1)
                
                labels.append(f"Semaine {week_num}\n{current_week_start.strftime('%d/%m')} - {week_end.strftime('%d/%m')}")
                
                start_week = timezone.make_aware(datetime.combine(current_week_start, datetime.min.time()))
                end_week = timezone.make_aware(datetime.combine(week_end, datetime.max.time()))
                
                weekly_reservations = Reservation.objects.filter(
                    created_at__range=[start_week, end_week]
                ).count()
                
                data.append(weekly_reservations)
                
                current_week_start = week_end + timedelta(days=1)
                week_num += 1
                
                if current_week_start > today:
                    break
            
            chart_title = "Réservations par semaine"
            chart_subtitle = f"{self._get_month_name(today.month)} {today.year}"
            period_info = "Mois courant"
            
        elif period == 'month':
            # Données mois par mois pour l'année courante
            labels = []
            data = []
            
            for month in range(1, 13):
                month_name = self._get_month_name(month)
                labels.append(month_name)
                
                start_month = timezone.make_aware(datetime.combine(
                    today.replace(month=month, day=1), datetime.min.time()
                ))
                
                if month == 12:
                    end_month = timezone.make_aware(datetime.combine(
                        today.replace(year=today.year + 1, month=1, day=1) - timedelta(days=1), 
                        datetime.max.time()
                    ))
                else:
                    end_month = timezone.make_aware(datetime.combine(
                        today.replace(month=month + 1, day=1) - timedelta(days=1), 
                        datetime.max.time()
                    ))
                
                monthly_reservations = Reservation.objects.filter(
                    created_at__range=[start_month, end_month]
                ).count()
                
                data.append(monthly_reservations)
            
            chart_title = "Réservations par mois"
            chart_subtitle = str(today.year)
            period_info = "Année courante"
            
        elif period == 'year':
            # Données des 5 dernières années
            labels = []
            data = []
            
            for i in range(4, -1, -1):  # De -4 à 0 (5 années)
                year = today.year - i
                labels.append(str(year))
                
                start_year = timezone.make_aware(datetime.combine(
                    date(year, 1, 1), datetime.min.time()
                ))
                end_year = timezone.make_aware(datetime.combine(
                    date(year, 12, 31), datetime.max.time()
                ))
                
                yearly_reservations = Reservation.objects.filter(
                    created_at__range=[start_year, end_year]
                ).count()
                
                data.append(yearly_reservations)
            
            chart_title = "Réservations par année"
            chart_subtitle = f"{today.year - 4} - {today.year}"
            period_info = "5 dernières années"
        
        total = sum(data)
        
        return {
            'labels': labels,
            'data': data,
            'chart_title': chart_title,
            'chart_subtitle': chart_subtitle,
            'unit': 'nombre',
            'period_info': period_info,
            'total': total
        }
    
    def _get_day_name(self, weekday):
        """Retourner le nom du jour en français"""
        days = ['Lundi', 'Mardi', 'Mercredi', 'Jeudi', 'Vendredi', 'Samedi', 'Dimanche']
        return days[weekday]
    
    def _get_month_name(self, month):
        """Retourner le nom du mois en français"""
        months = [
            '', 'Janvier', 'Février', 'Mars', 'Avril', 'Mai', 'Juin',
            'Juillet', 'Août', 'Septembre', 'Octobre', 'Novembre', 'Décembre'
        ]
        return months[month]

class RoomStatusChartView(APIView):
    """API pour le graphique des états de chambres à l'instant T"""
    
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        try:
            # Obtenir le timestamp actuel
            now = timezone.now()
            
            # Calculer les statistiques des chambres
            # Chambres libres (propres + sales)
            chambres_libres_propres = Room.objects.filter(status='lp').count()
            chambres_libres_sales = Room.objects.filter(status='ls').count()
            chambres_libres = chambres_libres_propres + chambres_libres_sales
            
            # Chambres occupées (propres + sales + gratuites)
            chambres_occupees_propres = Room.objects.filter(status='op').count()
            chambres_occupees_sales = Room.objects.filter(status='os').count()
            chambres_occupees_gratuites = Room.objects.filter(status='og').count()
            chambres_occupees = chambres_occupees_propres + chambres_occupees_sales + chambres_occupees_gratuites
            
            # Chambres en nettoyage
            chambres_nettoyage = Room.objects.filter(status='nettoyage').count()
            
            # Chambres hors service
            chambres_hors_service = Room.objects.filter(status='hs').count()
            
            # Total des chambres
            total_chambres = Room.objects.count()
            
            # Calculer les pourcentages
            if total_chambres > 0:
                pourcentage_libres = Decimal((chambres_libres / total_chambres) * 100).quantize(Decimal('0.01'))
                pourcentage_occupees = Decimal((chambres_occupees / total_chambres) * 100).quantize(Decimal('0.01'))
                pourcentage_nettoyage = Decimal((chambres_nettoyage / total_chambres) * 100).quantize(Decimal('0.01'))
                pourcentage_hors_service = Decimal((chambres_hors_service / total_chambres) * 100).quantize(Decimal('0.01'))
            else:
                pourcentage_libres = Decimal('0.00')
                pourcentage_occupees = Decimal('0.00')
                pourcentage_nettoyage = Decimal('0.00')
                pourcentage_hors_service = Decimal('0.00')
            
            # Préparer les données pour le graphique
            chart_labels = ['Libres', 'Occupées', 'Nettoyage', 'Hors Service']
            chart_data = [chambres_libres, chambres_occupees, chambres_nettoyage, chambres_hors_service]
            chart_colors = ['#28a745', '#dc3545', '#ffc107', '#6c757d']  # Vert, Rouge, Jaune, Gris
            
            # Construire la réponse
            data = {
                'chambres_libres': chambres_libres,
                'chambres_occupees': chambres_occupees,
                'chambres_nettoyage': chambres_nettoyage,
                'chambres_hors_service': chambres_hors_service,
                'chambres_libres_propres': chambres_libres_propres,
                'chambres_libres_sales': chambres_libres_sales,
                'chambres_occupees_propres': chambres_occupees_propres,
                'chambres_occupees_sales': chambres_occupees_sales,
                'chambres_occupees_gratuites': chambres_occupees_gratuites,
                'total_chambres': total_chambres,
                'pourcentage_libres': pourcentage_libres,
                'pourcentage_occupees': pourcentage_occupees,
                'pourcentage_nettoyage': pourcentage_nettoyage,
                'pourcentage_hors_service': pourcentage_hors_service,
                'labels': chart_labels,
                'data': chart_data,
                'colors': chart_colors,
                'timestamp': now.isoformat(),
                'last_updated': now.isoformat()
            }
            
            return Response(data, status=status.HTTP_200_OK)
            
        except Exception as e:
            return Response(
                {'error': f'Erreur lors du calcul des statistiques des chambres: {str(e)}'}, 
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
