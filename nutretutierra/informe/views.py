from rest_framework import generics
from serializers import informeserializers
from .models import informe

class informeList (generics.ListAPIView):
    queryset = informe.objects.all()
    serializer_class = informeserializers

class informeCreate (generics.CreateAPIView):
    queryset = informe.objects.all()
    serializer_class = informeserializers

class informeRetrieve (generics.RetrieveAPIView):
    queryset = informe.objects.all()
    serializer_class = informeserializers

class informeUpgrade (generics.UpdateAPIView):
    queryset = informe.objects.all()
    serializer_class = informeserializers

class informeDestroy (generics.DestroyAPIView):
    queryset = informe.objects.all()
    serializer_class = informeserializers
