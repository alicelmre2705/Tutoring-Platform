from django.db import models

# Create your models here.

class Language(models.Model):
    name = models.CharField(max_length=40)
    level = models.CharField(max_length=40)
    
    def __str__(self):
        return self.name
    
    
class Cours(models.Model):
    date = models.DateField(auto_now=False, auto_now_add=False)
    duration = models.DurationField()
    time_start = models.TimeField(auto_now=False, auto_now_add=False)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    id_language = models.ForeignKey(Language, on_delete=models.CASCADE) 
    
       
class Student(models.Model):
    username = models.CharField(max_length=200, unique=True)
    last_name = models.CharField(max_length=200, unique=False)
    first_name = models.CharField(max_length=200, unique=False)
    promotion = models.CharField(max_length= 5, unique=False)
    mail = models.EmailField(max_length=450)
    id_language = models.ManyToManyField(Language, related_name='language', blank=True)
    id_cours = models.ManyToManyField(Cours, related_name='cours', blank=True)
    
    def __str__(self):
        return self.username



    
    
    