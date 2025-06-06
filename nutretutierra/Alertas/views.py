from rest_framework import generics
from .serializers import alertaserializers
from .models import configuracionalerta

class configalertaList(generics.ListAPIView):
    queryset = configuracionalerta.objects.all()
    serializer_class = configuracionalerta

class configalertaCreate(generics.CreateAPIView):
    queryset = configuracionalerta.objects.all()
    serializer_class = configuracionalerta

class configalertaRetrieve(generics.RetrieveAPIView):
    queryset = configuracionalerta.objects.all()
    serializer_class = configuracionalerta

class configalertaUpdate(generics.UpdateAPIView):
    queryset = configuracionalerta.objects.all()
    serializer_class = configuracionalerta

class configalertaDestroy(generics.DestroyAPIView):
    queryset = configuracionalerta.objects.all()
    serializer_class = configuracionalerta

# Create your views here.
