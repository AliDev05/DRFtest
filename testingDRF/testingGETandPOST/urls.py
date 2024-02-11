from django.urls import path
from django.urls import re_path
from .views import ConverterRetrieveAPIView, ConverterCreateAPIView, DateTimeLetterFilterAPIView, DateTimePositionFilterAPIView

urlpatterns = [
    path('api/retreive/<int:id>/', ConverterRetrieveAPIView.as_view(), name='retreive'),
    path('api/create/', ConverterCreateAPIView.as_view(), name='create'),
    re_path(r'^api/datetime/(?P<datetimedigits>\d{1,3}[wdhms])/$', DateTimeLetterFilterAPIView.as_view()),
    re_path(r'^api/datetimeposition/(?P<datetimedigits>\d{1,2}:\d{1,2}:\d{1,2}:\d{1,2}:\d{1,2}:\d{1,2})/$', DateTimePositionFilterAPIView.as_view())
]