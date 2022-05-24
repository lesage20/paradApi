from django.db.models.signals  import post_save
from django.dispatch import receiver 
from django.contrib.auth.models import User #, Group
from .models import Profil 



@receiver(signal=post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        # group = Group.objects.get(name='customer')
        # instance.groups.add(group)
        Profil.objects.create(user=instance, name=instance.username, email=instance.email)
        print('profile created successfully')   