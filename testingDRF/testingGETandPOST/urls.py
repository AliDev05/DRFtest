from django.urls import path
from django.urls import re_path
from .views import ConverterRetrieveAPIView, ConverterCreateAPIView, DateAPIView, TimeAPIView

urlpatterns = [
    path('api/retreive/<int:id>/', ConverterRetrieveAPIView.as_view(), name='retreive'),
    path('api/create/', ConverterCreateAPIView.as_view(), name='create'),
    re_path(r'^api/date/(?P<datedigits>\d{1,3}[wd])/$', DateAPIView.as_view()),
    re_path(r'^api/time/(?P<timedigits>\d{1,3}[hms])/$', TimeAPIView.as_view()),
]