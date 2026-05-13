from django.db import models
from users.models import User
from reports.models import Reports

# Create your models here.
class DataSet(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='DataSource'
    )

    file_name = models.CharField(max_length=255)
    file      = models.FileField()

    def __str__(self):
        return self.file_name
    
class KPI(models.Model):
    report = models.ForeignKey(
        Reports,
        on_delete=models.CASCADE,
        related_name='KPI'
    )

    label = models.CharField(max_length=255)
    value = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)