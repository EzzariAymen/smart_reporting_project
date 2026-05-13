from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    ROLE_CHOICES = [('mgr', 'Manager'), 
                    ('eng', 'Engineer'), 
                    ('usr', 'User')]
    role = models.CharField(choices=ROLE_CHOICES, max_length=10)

    def __str__(self):
        return f"{self.prenom} {self.nom} ({self.username})"
    
class Notification(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='Notifications'
    )

    message    = models.TextField()
    is_read    = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Notification pour {self.user.username}"