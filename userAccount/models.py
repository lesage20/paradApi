from email.policy import default
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Profil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    avatar = models.ImageField(upload_to="avatars/", default="avatars/usericon.png", null=True, blank=True)
    phone = models.CharField(max_length=50, null=True, blank=True) 
    name = models.CharField(max_length=50, null=True, blank=True) 
    email = models.CharField(max_length=250, null=True, blank=True) 
    
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, auto_now_add=False)

    class Meta:
        verbose_name = "Profil utilisateur"
        verbose_name = "Profils  utilisateur"

    def __str__(self) -> str:
        return self.name or 'user ' + str(self.pk)
