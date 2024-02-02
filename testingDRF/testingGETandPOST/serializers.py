from rest_framework import serializers
from .models import Converter


class ConverterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Converter
        fields = '__all__'