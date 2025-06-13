from django.db import models
from django.contrib.auth.models import User
from userAccount.models import Profil
from uuid import uuid4
import datetime
floorStatus = [
    ('actif', 'Actif',),
    ('inactif', 'Inactif',)
]
guestGenders = [
    ('homme', 'Homme',),
    ('femme', 'Femme',)
]

bookingStatus = [
    ('ongoing', 'En cours',),
    ('completed', 'Terminée',),
    # ('cancelled', 'Annulée',)
]
paymentStatus = [
    ('pj', 'Payé jour',),
    ('dj', 'Dette jour',),
    ('dt', 'Dette totale',),
    ('dp', 'Dette payée',),
]
payment = [
    ('espece', 'Espèce',),
    ('cheque', 'Chèque',),
    ('visa', 'Visa',),
    ('devise', 'Devise',),
]
reservationStatus = [
    ('en attente', 'En attente',),
    ('confirmée', 'Confirmée',),
    ('annulée', 'Annulée',)
]

roomStatus = [
    ('os', 'Occupée Sale',),
    ('og', 'Occupée Gratuite',),
    ('op', 'Occupée Propre',),
    ('lp', 'Libre Propre',),
    ('ls', 'Libre Sale',),
    ('nettoyage', 'Nettoyage',)
]
couponType = [
    ('fixe', 'Fixe',),
    ('pourcentage', 'Pourcentage',)
]
class Floor(models.Model):
    """Gestion de niveau d'étage."""

    name = models.CharField( max_length=100, unique=True)
    description = models.TextField()
    number = models.IntegerField( unique=True)
    status = models.CharField( max_length=7, choices=floorStatus)
    
    created_at = models.DateTimeField( auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        """Affichage des niveaux d'étage dans la bd"""

        verbose_name = 'Etage'
        verbose_name_plural = 'Etages'

    def __str__(self):
        """Unicode representation of Floor."""
        return f'étage {self.number}' if self.number else "Bas de l'étage"
    def get_count(self):
        return self.objects.all().count

class RoomType(models.Model):
    """Gestion des types de chambre."""

    # TODO: Define fields here
    name = models.CharField( max_length=100, unique=True)
    description = models.TextField()
    numberAdult = models.IntegerField( default=1)
    numberChildren = models.IntegerField( default=0)
    price = models.IntegerField()
    
    created_at = models.DateTimeField( auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        """Meta definition for RoomType."""

        verbose_name = 'Type de Chambre'
        verbose_name_plural = 'Type de Chambres'

    def __str__(self):
        """Unicode representation of RoomType."""
        return self.name

    def get_count(self):
        return self.objects.all().count

class Room(models.Model):
    """Gestion des chambres."""

    # TODO: Define fields here
    number = models.CharField(max_length=5)
    floor = models.ForeignKey(Floor, on_delete=models.CASCADE, related_name='rooms')
    type = models.ForeignKey(RoomType, on_delete=models.CASCADE, related_name='rooms')
    status = models.CharField( max_length=10,  choices=roomStatus, default="lp")

    created_at = models.DateTimeField( auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        """Affichage des chambres dans la bd."""
        verbose_name = 'Chambre'
        verbose_name_plural = 'Chambres'

    def __str__(self):
        return self.number 

    def get_count(self):
        return self.objects.all().count

class Coupon(models.Model):
    """Gestion des coupons de réduction."""

    # TODO: Define fields here
    title = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)
    discount = models.IntegerField(default=0)
    type = models.CharField(max_length=12, choices=couponType, default="fixe")
    code = models.CharField(max_length=10)

    created_at = models.DateTimeField( auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        """Affichage des coupons de réduction dans la bd."""

        verbose_name = 'Coupon'
        verbose_name_plural = 'Coupons'

    def __str__(self):
        return self.title
    def get_count(self):
        return self.objects.all().count


class Booking(models.Model):
    """Gestion des location."""

    # TODO: Define fields here
    reference = models.CharField(max_length=10, null=True, blank=True, unique=True)
    guest = models.ForeignKey(Profil, on_delete=models.CASCADE, related_name='bookings_guest')
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='bookings')
    coupon = models.ForeignKey(Coupon, on_delete=models.CASCADE, related_name='bookings', null=True, blank=True)
    checkIn = models.DateTimeField()
    checkOut = models.DateTimeField()
    adults = models.IntegerField(default=1)
    children = models.IntegerField(default=0)
    status = models.CharField(max_length=15, choices=bookingStatus)
    totalPrice = models.IntegerField(default=0)
    amountPaid = models.IntegerField(default=0)
    amountDue = models.IntegerField(default=0)
    payment = models.CharField(max_length=15, choices=payment, default="espece")
    recorded_by = models.ForeignKey(Profil, on_delete=models.CASCADE, related_name='bookings_recorder')
    created_at = models.DateTimeField( auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    

    class Meta:
        """Affichage des locations."""
        verbose_name = 'Location'
        verbose_name_plural = 'Locations'

    def __str__(self):
        """Unicode representation of Booking."""
        return f'{self.room.number} loué par {self.guest.name} {self.guest.firstname} le {self.checkIn}'    
    
    def calculate_days(self):
        """
        Calcule le nombre de jours selon les règles suivantes :
        - Si le client arrive avant 4h :
          * Sortie avant 13h = 1 jour
          * Sortie après 13h = 2 jours
        - Si le client arrive après 4h :
          * Sortie avant 13h le lendemain = 1 jour
          * Sortie après 13h le lendemain = 2 jours
        - Pour les séjours de plusieurs jours :
          * Le jour d'arrivée compte comme un jour complet
          * Le jour de départ compte comme un jour complet si départ après 13h
        """
        # On normalise les dates pour ignorer l'heure d'arrivée
        check_in_date = self.checkIn.date()
        check_out_date = self.checkOut.date()
        
        # On vérifie les heures d'arrivée et de départ
        check_in_hour = self.checkIn.hour
        check_out_hour = self.checkOut.hour
        
        # Calcul du nombre de jours de base
        days = (check_out_date - check_in_date).days
        
        # Si c'est le même jour
        if check_in_date == check_out_date:
            if check_in_hour < 4:
                if check_out_hour >= 13:
                    days = 2
                else:
                    days = 1
            else:
                days = 1
        # Si c'est le lendemain
        elif (check_out_date - check_in_date).days == 1:
            if check_out_hour >= 13:
                days = 2
            else:
                days = 1
        # Si plus d'un jour
        else:
            # On ajoute un jour pour le jour d'arrivée
            days += 1
            # On ajoute un jour si départ après 13h
            if check_out_hour >= 13:
                days += 1
            
        return max(1, days)  # On retourne au minimum 1 jour

    def save(self, *args, **kwargs):
        if not self.reference:
            while True:
                ref = str(uuid4().hex)[:10]
                try: 
                    Booking.objects.get(reference=ref)
                except Booking.DoesNotExist:
                    self.reference = ref
                    break
        
        if not self.pk:  # Nouvelle instance
            self.status = 'pj'
            
        roomPrice = self.room.type.price
        if self.coupon:
            if self.coupon.type == 'fixe':
                roomPrice = self.room.type.price - self.coupon.discount
            else:  # type == 'pourcentage'
                if self.coupon.discount > 100:
                    self.coupon.discount = 100
                if self.coupon.discount < 0:
                    self.coupon.discount = 0
                    
                roomPrice = self.room.type.price * (1 - self.coupon.discount / 100)
        
        self.totalPrice = self.calculate_days() * roomPrice
        self.amountDue = self.totalPrice - self.amountPaid
        if (self.amountDue <= 0):
            self.amountDue = 0

        return super().save(*args, **kwargs)
    
    def get_count(self):
        return self.objects.all().count
    
class Payment(models.Model):
    booking = models.ForeignKey(Booking, on_delete=models.CASCADE, related_name='payments')
    amount = models.IntegerField()
    status = models.CharField(max_length=15, choices=paymentStatus)
    payment = models.CharField(max_length=15, choices=payment, default="espece")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = ("paiement")
        verbose_name_plural = ("paiements")

    def save(self, *args, **kwargs):
        # Calculer le nouveau montant total payé
        total_paid = sum(payment.amount for payment in self.booking.payments.all())
        # Mettre à jour le montant payé dans le booking
        self.booking.amountPaid = total_paid
        self.booking.save()
        super().save(*args, **kwargs)

class Facture(models.Model):
    booking = models.ForeignKey(Booking, on_delete=models.CASCADE, related_name='factures')
    amount = models.IntegerField()
    status = models.CharField(max_length=15, choices=bookingStatus)
    created_at = models.DateTimeField( auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = ("depense")
        verbose_name_plural =("depenses")

    def __str__(self):
        return f"{self.status} - {self.amount}"

class Depense(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    amount = models.IntegerField()
    date = models.DateField()
    spent_by = models.ForeignKey(Profil, on_delete=models.CASCADE, related_name='depenses')
    created_at = models.DateTimeField( auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = ("depense")
        verbose_name_plural =("depenses")

    def __str__(self):
        return self.title

class Reservation(models.Model):
    reference = models.CharField(max_length=10, null=True, blank=True, unique=True)
    guest = models.ForeignKey(Profil, on_delete=models.CASCADE, related_name='reservation_guest')
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='reservations')
    checkIn = models.DateTimeField()
    checkOut = models.DateTimeField()
    recorded_by = models.ForeignKey(Profil, on_delete=models.CASCADE, related_name='reservation_recorder')
    created_at = models.DateTimeField( auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=15, choices=reservationStatus, default="en attente")

    class Meta:
        verbose_name = "Reservation"
        verbose_name_plural = "Reservations"

    def __str__(self):
        return f"{self.room.number} Réservé le {self.checkIn}" 

    def save(self, *args, **kwargs):
        if not self.reference:
            while True:
                ref = str(uuid4().hex)[:10]
                try: 
                    Reservation.objects.get(reference=ref)
                except Reservation.DoesNotExist:
                    self.reference = ref
                    break
        
        return super().save(*args, **kwargs)

