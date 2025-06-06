from django.db import models

class configuracionalerta(models.Model):
    humedad_minima = models.FloatField(default=30.0, verbose_name="Humedad Mínima Aceptable (%)")
    humedad_maxima = models.FloatField(default=70.0, verbose_name="Humedad Máxima Aceptable (%)")
    ultima_actualizacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.humedad_minima
    