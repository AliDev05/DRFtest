from django.shortcuts import render
from .models import Converter
from .serializers import ConverterSerializer


from rest_framework.views import APIView
from rest_framework.generics import RetrieveAPIView, CreateAPIView


class ConverterRetrieveAPIView(RetrieveAPIView):
    queryset = Converter.objects.all()
    serializer_class = ConverterSerializer
    lookup_field = 'id'


class ConverterCreateAPIView(CreateAPIView):
    queryset = Converter.objects.all()
    serializer_class = ConverterSerializer