from django.urls import path

from.views import(
    informeList,
    informeCreate,
    informeDestroy,
    informeUpgrade,
    informeRetrieve,
)

urlpatterns =[
    path ("informelista /",informeList.as_view(), name="informeList"),
    path ("informeCreado/",informeCreate.as_view(), name="informeCreate"),
    path ("informeDestroy/",informeDestroy.as_view(), name="informeDetail"),
    path ("informeactualizar/", informeUpgrade.as_view(), name="informeUpgrade"),
    path ("informerecuperar/" ,informeRetrieve.as_view(), name="informeRetrieve"),
    
          
]