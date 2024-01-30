from django.db import models

from django.core.validators import MaxValueValidator


class Converter(models.Model):
	lat = models.FloatField()
	lng = models.FloatField()
	color = models.CharField(max_length=20)
	last_update = models.DateTimeField()
	failures = models.IntegerField()
	currently_running = models.BooleanField()
	L1_voltage = models.FloatField()
	L2_voltage = models.FloatField()
	L3_voltage = models.FloatField()
	input_current_L1 = models.FloatField()
	input_current_L2 = models.FloatField()
	input_current_L3 = models.FloatField()
	AC_freq = models.FloatField()
	output_DC_voltage = models.FloatField()
	total_DC_load_c = models.FloatField()
	total_battery_c = models.FloatField()
	battery_capacity = models.IntegerField() #Номинальная емкость аккумулятора 
	remaining_capacity = models.IntegerField() #Всего остаточной емкости
	remaining_capacity_percenteage =models.IntegerField(validators=[MaxValueValidator(100)])  