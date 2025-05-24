from rest_framework import generics
from serializers import cultivoserializers

class cultivoList(generics.ListAPIView):
    queryset = cultivo.objects.all()
    serializer_class = cultivoserializers

class cultivoCreate(generics.CreateAPIView):
    queryset = cultivo.objects.all()
    serializer_class = cultivoserializers

class cultivoRetrieve(generics.RetrieveAPIView):
    queryset = cultivo.objects.all()
    serializer_class = cultivoserializers

class cultivoUpdate(generics.UpdateAPIView):
    queryset = cultivo.objects.all()
    serializer_class = cultivoserializers

class cultivoDestroy(generics.DestroyAPIView):
    queryset = cultivo.objects.all()
    serializer_class = cultivoserializers
    


