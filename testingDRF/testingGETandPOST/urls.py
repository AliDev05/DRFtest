from django.urls import path
from .views import ConverterRetrieveAPIView, ConverterCreateAPIView, ConverterListAPIView

urlpatterns = [
    path('api/retreive/<int:id>/', ConverterRetrieveAPIView.as_view(), name='retreive'),
    path('api/create/', ConverterCreateAPIView.as_view(), name='create'),
    path('api/lasthour/', ConverterListAPIView.as_view(), name='lasthour')
]