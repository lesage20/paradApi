from rest_framework import serializers
from django.contrib.auth.models import User
from datetime import datetime, date


class UnifiedKPISerializer(serializers.Serializer):
    """Serializer unifié pour les KPIs qui s'adapte selon le rôle utilisateur"""
    
    # Filtres de période (pour admin uniquement)
    PERIOD_CHOICES = [
        ('today', 'Aujourd\'hui'),
        ('week', 'Cette semaine'),
        ('month', 'Ce mois'),
        ('quarter', 'Ce trimestre'),
        ('semester', 'Ce semestre'),
        ('year', 'Cette année'),
    ]
    
    # Méta-informations
    user_role = serializers.CharField(read_only=True)
    period = serializers.ChoiceField(choices=PERIOD_CHOICES, required=False)
    
    # KPIs communs
    revenu_total = serializers.DecimalField(max_digits=10, decimal_places=2, read_only=True, required=False)
    nombre_locations = serializers.IntegerField(read_only=True, required=False)
    
    # KPIs spécifiques Admin
    taux_occupation = serializers.DecimalField(max_digits=5, decimal_places=2, read_only=True, required=False)
    revpar = serializers.DecimalField(max_digits=10, decimal_places=2, read_only=True, required=False)
    
    # Données de comparaison Admin (période précédente)
    revenu_total_precedent = serializers.DecimalField(max_digits=10, decimal_places=2, read_only=True, required=False)
    taux_occupation_precedent = serializers.DecimalField(max_digits=5, decimal_places=2, read_only=True, required=False)
    revpar_precedent = serializers.DecimalField(max_digits=10, decimal_places=2, read_only=True, required=False)
    nombre_locations_precedent = serializers.IntegerField(read_only=True, required=False)
    
    # Évolution en pourcentage Admin
    evolution_revenu = serializers.DecimalField(max_digits=5, decimal_places=2, read_only=True, required=False)
    evolution_taux_occupation = serializers.DecimalField(max_digits=5, decimal_places=2, read_only=True, required=False)
    evolution_revpar = serializers.DecimalField(max_digits=5, decimal_places=2, read_only=True, required=False)
    evolution_locations = serializers.DecimalField(max_digits=5, decimal_places=2, read_only=True, required=False)
    
    # Informations sur la période Admin
    periode_debut = serializers.DateTimeField(read_only=True, required=False)
    periode_fin = serializers.DateTimeField(read_only=True, required=False)
    
    # KPIs spécifiques Gérant
    revenus_jour = serializers.DecimalField(max_digits=10, decimal_places=2, read_only=True, required=False)
    locations_actives = serializers.IntegerField(read_only=True, required=False)
    entrees_prevues = serializers.IntegerField(read_only=True, required=False)
    sorties_prevues = serializers.IntegerField(read_only=True, required=False)
    
    # Détails Gérant
    entrees_details = serializers.ListField(
        child=serializers.DictField(), 
        read_only=True,
        required=False
    )
    sorties_details = serializers.ListField(
        child=serializers.DictField(), 
        read_only=True,
        required=False
    )
    
    # Informations contextuelles
    date_du_jour = serializers.DateField(read_only=True, required=False)
    date_derniere_mise_a_jour = serializers.DateTimeField(read_only=True)


class PeriodFilterSerializer(serializers.Serializer):
    """Serializer pour filtrer par période personnalisée"""
    
    date_debut = serializers.DateTimeField(required=False)
    date_fin = serializers.DateTimeField(required=False)
    
    def validate(self, data):
        """Valider que la date de fin est après la date de début"""
        if data.get('date_debut') and data.get('date_fin'):
            if data['date_debut'] >= data['date_fin']:
                raise serializers.ValidationError(
                    "La date de fin doit être postérieure à la date de début"
                )
        return data


class DashboardSummarySerializer(serializers.Serializer):
    """Serializer pour le résumé du dashboard"""
    
    # Données générales
    total_chambres = serializers.IntegerField(read_only=True)
    chambres_occupees = serializers.IntegerField(read_only=True)
    chambres_libres = serializers.IntegerField(read_only=True)
    chambres_sale = serializers.IntegerField(read_only=True)
    
    # Revenus
    revenus_today = serializers.DecimalField(max_digits=10, decimal_places=2, read_only=True)
    revenus_month = serializers.DecimalField(max_digits=10, decimal_places=2, read_only=True)
    revenus_year = serializers.DecimalField(max_digits=10, decimal_places=2, read_only=True)
    
    # Locations
    locations_today = serializers.IntegerField(read_only=True)
    locations_month = serializers.IntegerField(read_only=True)
    locations_year = serializers.IntegerField(read_only=True)
    
    # Taux d'occupation
    taux_occupation_today = serializers.DecimalField(max_digits=5, decimal_places=2, read_only=True)
    taux_occupation_month = serializers.DecimalField(max_digits=5, decimal_places=2, read_only=True)
    taux_occupation_year = serializers.DecimalField(max_digits=5, decimal_places=2, read_only=True)
    
    # Données de contexte
    date_derniere_mise_a_jour = serializers.DateTimeField(read_only=True)


class ChartDataSerializer(serializers.Serializer):
    """Serializer pour les données de graphiques du dashboard"""
    
    CHART_TYPE_CHOICES = [
        ('revenus', 'Revenus'),
        ('occupation', 'Occupation'),
        ('reservations', 'Réservations'),
    ]
    
    PERIOD_CHOICES = [
        ('day', 'Jour par jour (semaine courante)'),
        ('week', 'Semaine par semaine (mois courant)'),
        ('month', 'Mois par mois (année courante)'),
        ('year', 'Année par année (5 dernières années)'),
    ]
    
    # Paramètres de la requête
    chart_type = serializers.ChoiceField(choices=CHART_TYPE_CHOICES)
    period = serializers.ChoiceField(choices=PERIOD_CHOICES)
    
    # Données de réponse
    labels = serializers.ListField(child=serializers.CharField(), read_only=True)
    data = serializers.ListField(child=serializers.DecimalField(max_digits=15, decimal_places=2), read_only=True)
    
    # Méta-informations
    chart_title = serializers.CharField(read_only=True)
    chart_subtitle = serializers.CharField(read_only=True)
    unit = serializers.CharField(read_only=True)  # 'FCFA', 'nombre', etc.
    period_info = serializers.CharField(read_only=True)
    total = serializers.DecimalField(max_digits=15, decimal_places=2, read_only=True)
    
    # Métadonnées pour l'échelle des graphiques
    min_value = serializers.DecimalField(max_digits=15, decimal_places=2, read_only=True)
    max_value = serializers.DecimalField(max_digits=15, decimal_places=2, read_only=True)
    suggested_step = serializers.DecimalField(max_digits=15, decimal_places=2, read_only=True)
    suggested_max = serializers.DecimalField(max_digits=15, decimal_places=2, read_only=True)
    
    # Informations de contexte
    generated_at = serializers.DateTimeField(read_only=True) 