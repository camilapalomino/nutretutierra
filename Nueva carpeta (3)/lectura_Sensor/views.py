from rest_framework import generics
from .serializers import lectura_sensor
from .models import lectura_sensor

class lecturaCreate (generics.CreateAPIView):
    queryset = lectura_sensor.objects.all()
    serializer_class = lectura_sensor

class lecturaRetrieve (generics.RetrieveAPIView):
    queryset = lectura_sensor.objects.all()
    serializer_class = lectura_sensor

class lecturaUpdate (generics.UpdateAPIView):
    queryset = lectura_sensor.objects.all()
    serializer_class = lectura_sensor

# Create your views here.
