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
    # user config
    role = models.ForeignKey(Group, on_delete=models.CASCADE, related_name='profils', null=True, blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    # about the person
    avatar = models.ImageField(upload_to="avatars/", default="avatars/usericon.png", blank=True)
    name = models.CharField(max_length=50) 
    firstname = models.CharField(max_length=100)
    gender = models.CharField(max_length=50, choices=genders)
    phone = models.CharField(max_length=50) 
    email = models.CharField(max_length=250, null=True, blank=True) 
    address = models.CharField(max_length=50, null=True, blank=True)
    dob = models.DateField()
    place_of_birth = models.CharField(max_length=50, null=True)
    department = models.CharField(max_length=50, null=True)  
    nationnalite = models.CharField(max_length=50, null=True)
    job = models.CharField(max_length=50, null=True)
    domicile = models.CharField(max_length=150, null=True)

    # Id details
    idType = models.CharField(max_length=50, choices=idTypes)
    idNumber = models.CharField(max_length=20)
    id_delivered_at = models.DateField(auto_now=False, auto_now_add=False)
    id_delivered_place = models.CharField(max_length=150)
    id_delivered_by = models.CharField(max_length=150)
    # Parent details
    father = models.CharField(max_length=150, null=True)
    mother = models.CharField(max_length=150, null=True)

    

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

        if self.role.name == "client":
            if any( not i for i in  [self.id_delivered_at ,self.id_delivered_place ,self.id_delivered_by ,self.father ,
                self.mother ,self.nationnalite ,self.job ,self.domicile ]):
                
                raise ValueError("Données manquante", "Pour les client certaines informations sont obligatoire veuillez toutes les remplir ")
                


        return super().save(*args, **kwargs)
    
    def __str__(self) -> str:
        return f'{self.name} {self.firstname}' or self.user.username or f'user {self.pk}'
    

