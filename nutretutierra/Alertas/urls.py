from django.urls import path
from .views import(
    configalertaList,
    configalertaCreate,
    configalertaDestroy,
    configalertaRetrieve,
    configalertaUpdate
)

urlpatterns = [
    path ("configlista/", configalertaList.as_view(), name="configList"),
    path ("configcrear/", configalertaCreate.as_view(), name="configCreate"),
    path ("configborrar/", configalertaDestroy.as_view(), name="configDestroy"),
    path ("configAct/", configalertaRetrieve.as_view(), name="configRetrieve"),
    path ("configTall/", configalertaUpdate.as_view(), name="configUpdate"),
    
]