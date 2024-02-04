from datetime import datetime, timedelta

from .models import Converter
from .serializers import ConverterSerializer

from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import RetrieveAPIView, CreateAPIView, ListAPIView


class ConverterRetrieveAPIView(RetrieveAPIView):
    queryset = Converter.objects.all()
    serializer_class = ConverterSerializer
    lookup_field = 'id'


class ConverterCreateAPIView(CreateAPIView):
    queryset = Converter.objects.all()
    serializer_class = ConverterSerializer


class ConverterListAPIView(ListAPIView):
    serializer_class = ConverterSerializer

    def get_queryset(self):
        end_datetime = datetime.now()
        start_datetime = end_datetime - timedelta(hours=1)

        queryset = Converter.objects.filter(
            last_update_date=start_datetime.date(),
            last_update_time__gte=start_datetime.time(),
            last_update_time__lt=end_datetime.time()
        )

        return queryset