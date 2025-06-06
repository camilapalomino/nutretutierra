from django.db import models

class informe (models.Model):
    titulo = models.CharField()
    informacion = models.CharField()
    generacion = models.DateField()
    alerta = models.BooleanField()

    def __str__(self):
        return self.titulo


