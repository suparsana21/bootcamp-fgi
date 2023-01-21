from django.db import models

# Create your models here.

class User(models.Model):
    
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, null=False, blank=False)
    username = models.CharField(max_length=50, null=False, blank=False, unique=True)
    password = models.CharField(max_length=100, null=False, blank=False)

    class Meta:
        db_table = 'users'
        
        