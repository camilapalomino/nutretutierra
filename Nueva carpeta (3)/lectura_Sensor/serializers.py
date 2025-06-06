from rest_framework import serializers
from models import lectura_sensor

class serielizerLecturaSensor(serializers.ModelSerializer):
    class Meta:
        model = lectura_sensor
        fields = ['sensor', 'valor', 'fecha']