from django.db import models

# Create your models here.
class lectura_sensor(models.Model):
    lectura_sensor = models.CharField() 
    valor = models.FloatField() #lector humedad
    fecha = models.DateTimeField (auto_now_add=True) #fecha de la lectura


    def __str__(self):
        return lectura_sensor