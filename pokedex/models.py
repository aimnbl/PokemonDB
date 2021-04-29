from django.db import models

# Create your models here.

class Type(models.Model):
    type= models.CharField(max_length=100)

class Pokemon(models.Model):
    pokedex_no= models.DecimalField(max_digits=4, decimal_places=0)
    name= models.CharField(max_length=100)
    generation= models.DecimalField(max_digits=2, decimal_places=0)  
    status = models.CharField(max_length=30)
    species = models.CharField(max_length=30)
    no_type = models.DecimalField(max_digits=2, decimal_places=0)
    type_1 = models.ForeignKey(Type, on_delete=models.CASCADE, related_name='type_1')
    type_2 = models.ForeignKey(Type, on_delete=models.CASCADE, blank=True, related_name='type_2')
    height = models.DecimalField(max_digits=5, decimal_places=2) 
    weight = models.DecimalField(max_digits=5, decimal_places=2)
    total_point = models.DecimalField(max_digits=5, decimal_places=0)
    hp = models.DecimalField(max_digits=4, decimal_places=0)
    attack = models.DecimalField(max_digits=4, decimal_places=0)
    defense = models.DecimalField(max_digits=4, decimal_places=0)
    sp_attack = models.DecimalField(max_digits=4, decimal_places=0)
    sp_defense = models.DecimalField(max_digits=4, decimal_places=0)
    speed = models.DecimalField(max_digits=4, decimal_places=0)