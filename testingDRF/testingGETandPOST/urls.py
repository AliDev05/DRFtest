from django.urls import path
from django.urls import re_path
from .views import ConverterRetrieveAPIView, ConverterCreateAPIView, DateTimeAPIView

urlpatterns = [
    path('api/retreive/<int:id>/', ConverterRetrieveAPIView.as_view(), name='retreive'),
    path('api/create/', ConverterCreateAPIView.as_view(), name='create'),
    re_path(r'^api/datetime/(?P<datetimedigits>\d{1,3}[wdhms])/$', DateTimeAPIView.as_view())
]