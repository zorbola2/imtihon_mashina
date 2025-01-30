from django.db import models

class Brand(models.Model):
    name = models.CharField(max_length=250)
    
    def __str__(self):
        return self.name

class Cars(models.Model):
    nomi = models.CharField(max_length=250)
    descriptions = models.TextField()
    price = models.FloatField()
    image = models.URLField(blank=True)
    brand_id = models.ForeignKey(Brand, on_delete=models.CASCADE)
    year = models.IntegerField()
    horse_power = models.IntegerField()
    korobka = models.CharField(max_length=250, choices=(('avtomat', 'avtomat'), ('mexanika', 'mexanika')))
    
    def __str__(self):
        
        return self.nomi
 

