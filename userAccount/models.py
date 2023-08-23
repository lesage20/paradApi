from email.policy import default
from django.db import models
from django.contrib.auth.models import User, Group
# Create your models here.

genders = [
    ('homme', 'Homme',),
    ('femme', 'Femme',)
]
idTypes = [
    ('cni', "Carte Nationale d'identité",),
    ('passeport', 'Passeport',),
    ('attestation', "Attestation d'identité",)
    
]
class Profil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    avatar = models.ImageField(upload_to="avatars/", default="avatars/usericon.png", blank=True)
    name = models.CharField(max_length=50) 
    firstname = models.CharField(max_length=100)
    gender = models.CharField(max_length=50, choices=genders)
    phone = models.CharField(max_length=50) 
    email = models.CharField(max_length=250, null=True, blank=True) 
    address = models.CharField(max_length=50, null=True, blank=True)
    dob = models.DateField()
    idType = models.CharField(max_length=50, choices=idTypes)
    idNumber = models.CharField(max_length=20)
    role = models.ForeignKey(Group, on_delete=models.CASCADE, related_name='profils', null=True, blank=True)
    department = models.CharField(max_length=50, null=True, blank=True)  
    
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, auto_now_add=False)

    class Meta:
        verbose_name = "Profil utilisateur"
        verbose_name = "Profils  utilisateur"
    
    def save(self, *args, **kwargs):
        if not self.user:
            self.role = Group.objects.get(name="client")
        else:
            self.role = self.user.groups.all()[0]
        return super().save(*args, **kwargs)
    
    def __str__(self) -> str:
        return f'{self.name} {self.firstname}' or self.user.username or f'user {self.pk}'
    

