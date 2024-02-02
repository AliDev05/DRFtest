from django.urls import path
from .views import ConverterRetrieveAPIView

urlpatterns = [
    path('api/retreive/<int:id>/', ConverterRetrieveAPIView.as_view(), name='get-converter'),
]