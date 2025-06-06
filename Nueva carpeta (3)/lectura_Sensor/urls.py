from django.urls import path

from.views import(
    lecturaCreate,
    lecturaRetrieve,
    lecturaUpdate,
)

urlpatterns = [
    path ("lecturacrear/", lecturaCreate.as_view(), name="lecturaCreate"),
    path ("lecturaRetrieve/", lecturaRetrieve.as_view(), name="lecturaRetrieve"),
    path ("lecturaUpdate/", lecturaUpdate.as_view(), name="lecturaUpdate"), 
]