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
    ('pj', 'Payé jour',),
    ('dj', 'Dette jour',),
    ('dt', 'Dette totale',),
    ('dp', 'Dette payée',),
    ('archive', 'Archivée',)
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
    description = models.TextField()
    discount = models.IntegerField(default=0)
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
    
    def save(self, *args, **kwargs):
        if not self.reference:
            while True:
                ref = str(uuid4().hex)[:10]
                try: 
                    Booking.objects.get(reference=ref)
                except Booking.DoesNotExist:
                    self.reference = ref
                    break
        if not self.totalPrice:
            if (self.checkOut -  self.checkIn) <= datetime.timedelta(days= 1):
                self.totalPrice = self.room.type.price
            else:
                self.totalPrice = (self.checkOut -  self.checkIn).days * self.room.type.price
        return super().save(*args, **kwargs)
    
    def get_count(self):
        return self.objects.all().count
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
