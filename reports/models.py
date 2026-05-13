from django.db import models
from users.models import User 

# Create your models here.
class Reports(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='reports'
    )

    title       = models.CharField(max_length=255)
    descreption = models.TextField()

    created_at  = models.DateTimeField(auto_now_add=True)
    uploaded_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title