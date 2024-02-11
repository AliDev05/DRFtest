from datetime import datetime, timedelta

from .models import Converter
from .serializers import ConverterSerializer

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import RetrieveAPIView, CreateAPIView, ListAPIView



class ConverterRetrieveAPIView(RetrieveAPIView):
    queryset = Converter.objects.all()
    serializer_class = ConverterSerializer
    lookup_field = 'id'


class ConverterCreateAPIView(CreateAPIView):
    queryset = Converter.objects.all()
    serializer_class = ConverterSerializer




class DateTimeLetterFilterAPIView(APIView):
    serializer_class = ConverterSerializer

    def get(self, request, datetimedigits):
        end_datetime = datetime.now()

        num = int(datetimedigits[:len(datetimedigits)-1])
        let = datetimedigits[-1]

        if let == 'w':
            start_datetime = end_datetime - timedelta(weeks=num)
        elif let == 'd':
            start_datetime = end_datetime - timedelta(days=num)
        elif let == 'h':                                                        # <--- Метод с указанием 
            start_datetime = end_datetime - timedelta(hours=num)
        elif let == 'm':
            start_datetime = end_datetime - timedelta(minutes=num)
        else:
            start_datetime = end_datetime - timedelta(seconds=num)
            


        queryset = Converter.objects.filter(
            last_update_datetime__gte=start_datetime,
            last_update_datetime__lte=end_datetime
        )


        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)




from dateutil.relativedelta import relativedelta


class DateTimePositionFilterAPIView(APIView):
    serializer_class = ConverterSerializer

    def get(self, request, datetimedigits):
        
        datetime_list = datetimedigits.split(':')           # <--- Позиционный метод

        end_datetime = datetime.now()
        date_to_subtract = relativedelta(years=+int(datetime_list[0]), months=+int(datetime_list[1]), days=int(datetime_list[2]), hours=+int(datetime_list[3]), minutes=+int(datetime_list[4]), seconds=+int(datetime_list[5]) )
        start_datetime = end_datetime - date_to_subtract


        queryset = Converter.objects.filter(
            last_update_datetime__gte=start_datetime,
            last_update_datetime__lt=end_datetime
        )
        
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)




class DateSegmentFilterAPIView(APIView):
    serializer_class = ConverterSerializer

    def get(self, request, datedigits):

        start_date, end_date = datedigits.split(":")            # <--- Метод указания отрезка даты

        queryset = Converter.objects.filter(
            last_update_datetime__gte=start_date,
            last_update_datetime__lt=end_date
            )

        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)