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




class DateAPIView(APIView):
    serializer_class = ConverterSerializer

    def get(self, request, datedigits):
        end_date = datetime.now().date()

        num = int(datedigits[:len(datedigits)-1])
        let = datedigits[-1]

        if let == 'w':
            start_date = end_date - timedelta(weeks=num)
        else :
            start_date = end_date - timedelta(days=num)



        queryset = Converter.objects.filter(
            last_update_date__gte=start_datetime,
            last_update_date__lte=end_datetime,
        )


        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)


"""class TimeAPIView(APIView):
    serializer_class = ConverterSerializer

    def get(self, request, timedigits):
        end_time = datetime.now()

        num = int(timedigits[:len(timedigits)-1])
        let = timedigits[-1]

        if let == 'h':
            start_time = end_time - timedelta(hours=num)
        elif let == 'm' :
            start_time = end_time - timedelta(minutes=num)
        else :
            start_time = end_time - timedelta(seconds=num)

        print(start_time)
        print(end_time)


        queryset = Converter.objects.filter(
            last_update_time__gte=start_time,
            last_update_time__lte=end_time
        )


        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)
"""



"""class DateTimeAPIView(ListAPIView):
    serializer_class = ConverterSerializer

    def get_queryset(self):
        datetimedigits = self.kwargs['datetime']
        end_datetime = datetime.now()

        num = int(datetimedigits[:len(datetimedigits)-1])
        let = datetimedigits[-1]

        


        if let == 'w':
            start_datetime = end_datetime - timedelta(weeks=num)
        elif let == 'd':
            start_datetime = end_datetime - timedelta(days=num)
        elif let == 'h':
            start_datetime = end_datetime - timedelta(hours=num)
        elif let == 'm':
            start_datetime = end_datetime - timedelta(minutes=num)
        else :
            start_datetime = end_datetime - timedelta(seconds=num)

            
        queryset = Converter.objects.filter(
            last_update_date__gte=start_datetime.date(),
            last_update_date__lt=end_datetime.date(),
            last_update_time__gte=start_datetime.time(),
            last_update_time__lt=end_datetime.time()
        )

        return queryset

"""




#from dateutil.relativedelta import relativedelta

"""class DateFilterAPIView(ListAPIView):
    serializer_class = ConverterSerializer

    def get_queryset(self):
        datedigits = self.kwargs['datedigits']
        year = int(datedigits[:2])
        month = int(datedigits[2:4])
        day = int(datedigits[4:6])

        end_date = datetime.now().date()
        date_to_subtract = relativedelta(years=year, months=month, days=day)
        start_date = end_date - date_to_subtract

        queryset = Converter.objects.filter(
            last_update_date__gte=start_date,
            last_update_date__lt=end_date
        )
        return queryset
"""