from django.db import models

# Create your models here.

# Todo:
#     - id: primary key
#     - category_id: priority (HIGH, MEDIUM, LOW)
#     - message
#   Category:
#       - id: primary key
#       - name: nama kategori

class Category(models.Model):
    id = models.IntegerField(primary_key=True, unique=True, null=False)
    name = models.CharField(max_length=50, null=False, blank=False)    
    
    class Meta:
        db_table = 'categories'
        

class Todo(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, null=False, blank=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    
    class Meta:
        db_table = 'todos'