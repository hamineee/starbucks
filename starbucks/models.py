from django.db import models

# Create your models here.
class Menu(models.Model):
    name = models.CharField(max_length=45)
    def __str__(self):
        return self.name

class Categories(models.Model):
    name = models.CharField(max_length=45)
    menu = models.ForeignKey(Menu, on_delete = models.CASCADE, null=True)
    def __str__(self):
        return self.name
        
class Drinks(models.Model):
    category        = models.ForeignKey(Categories, on_delete=models.CASCADE, null=True)
    nutrition      = models.OneToOneField('Nutrition', on_delete=models.CASCADE)
    korean_name     = models.CharField(max_length=45)
    english_name    = models.CharField(max_length=45)
    description     = models.TextField(null=True)
    allergy         = models.ManyToManyField('Allergy', through= 'AllergyDrink')
    def __str__(self):
        return self.korean_name

class Nutrition(models.Model):
    one_serving_kcal    = models.DecimalField(max_digits=6,decimal_places=2)
    sodium_mg           = models.DecimalField(max_digits=6,decimal_places=2)
    saturated_fat_g     = models.DecimalField(max_digits=6,decimal_places=2)
    sugars_g            = models.DecimalField(max_digits=6,decimal_places=2)
    protein_g           = models.DecimalField(max_digits=6,decimal_places=2)
    caffeine_mg         = models.DecimalField(max_digits=6,decimal_places=2)

class Size(models.Model):
    name             = models.CharField(max_length=45)
    size_ml          = models.IntegerField(default = 0)
    size_fluid_ounce = models.DecimalField(max_digits=10, decimal_places=2)
    nutrition        = models.ForeignKey('Nutrition', on_delete = models.SET_NULL, null=True)


class Images(models.Model):
    drink       = models.ForeignKey(Drinks, on_delete = models.CASCADE, null=True)
    image_url   = models.CharField(max_length=2000)
    def __str__(self):
        return self.image_url


class Allergy(models.Model):
    name = models.CharField(max_length=45)
    def __str__(self):
        return self.name

class AllergyDrink(models.Model):
    allergy = models.ForeignKey('Allergy', on_delete =  models.SET_NULL, null=True) 
    drink   = models.ForeignKey('Drinks', on_delete = models.SET_NULL, null=True)

