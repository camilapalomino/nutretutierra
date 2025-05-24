from django.db import models

# Create your models here.


class requerimiento (models.Model):
    tipo = models.CharField ()
    tipo_de_terreno = models.CharField ()
    Fecha_de_siembra = models.DateField ()