from django.db import models

# Create your models here.

class AvailableVoter(models.Model):
    fullname = models.CharField(max_length=200)
    email = models.CharField(max_length=100, unique=True)
    new = models.BooleanField(default=True)
    status = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering=('id','fullname','email',)           
