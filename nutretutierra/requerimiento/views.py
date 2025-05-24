from rest_framework import generics
from serializers import requerimiento

class requerimientoList(generics.ListAPIView):
    queryset = cultivo.objects.all()
    serializer_class = requerimiento

class requerimientoCreate(generics.CreateAPIView):
    queryset = cultivo.objects.all()
    serializer_class = requerimiento

class requerimientoRetrieve(generics.RetrieveAPIView):
    queryset = cultivo.objects.all()
    serializer_class = requerimiento

class requerimientoUpdate(generics.UpdateAPIView):
    queryset = cultivo.objects.all()
    serializer_class = requerimiento

class requerimientoDestroy(generics.DestroyAPIView):
    queryset = cultivo.objects.all()
    serializer_class = requerimiento