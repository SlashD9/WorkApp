from django.db import models
from .choices import Choices

# Create your models here.
class Site(models.Model):
    site_name = models.CharField(max_length=40)
    address = models.CharField(max_length=40, blank=True)
    town = models.CharField(max_length=40, blank=True)
    county = models.CharField(max_length=40, blank=True)
    country = models.CharField(max_length=40, blank=True)
    aircode = models.CharField(max_length=40, blank=True)

    def __str__(self):
        return str(self.site_name)

class Customer(models.Model):
    site_name = models.ForeignKey(Site, on_delete=models.CASCADE)
    customer_name = models.CharField(max_length=60)
    customer_email = models.EmailField()
    customer_phone = models.IntegerField()

class Pricing(models.Model):
    site_name = models.ForeignKey(Site, on_delete=models.CASCADE)
    call_out_charge = models.FloatField(blank=True)
    per_hour_charge = models.FloatField(blank=True)
    service_charge = models.FloatField(blank=True)

class Worksheet(models.Model):
    site_name = models.ForeignKey(Site, on_delete=models.CASCADE)
    date = models.DateField()
    start_time = models.TimeField(blank=True )
    end_time = models.TimeField(blank=True )
    travel_time = models.FloatField(blank=True)
    job_type = models.CharField(max_length=50, choices=Choices.JOB_TYPE)
    description = models.TextField()
    materials = models.TextField(blank=True)
    num_electrcians = models.IntegerField()
    num_apprentices = models.IntegerField()
    electricians_name = models.CharField(max_length=30)
    customer_name = models.CharField(max_length=50)
    customer_signature = models.CharField(max_length=50)
    status = models.CharField(max_length=50, choices=Choices.STATUS, default="Created")
    signature = models.ImageField(blank=True)
    image2 = models.ImageField(blank=True)
    image3 = models.ImageField(blank=True)
    image4 = models.ImageField(blank=True)
    image5 = models.ImageField(blank=True)
    image6 = models.ImageField(blank=True)


class Service(models.Model):
    site_name = models.ForeignKey(Site, on_delete=models.CASCADE)
    date = models.DateField()
    location = models.CharField(max_length=100)
    door_Code = models.CharField(max_length=20)
    installation_type = models.CharField(max_length=50, choices=Choices.INSTALLATION)
    controller_type =models.CharField(max_length=30)
    controller_condition = models.CharField(max_length=50, choices=Choices.CONDITION)
    selector_type = models.CharField(max_length=50, choices=Choices.SELECTOR)
    selector_other = models.CharField(max_length=50, blank=True)
    door_type = models.CharField(max_length=50, choices=Choices.DOOR_TYPE)
    door_condition = models.CharField(max_length=50, choices=Choices.CONDITION)
    arm_type = models.CharField(max_length=50, choices=Choices.ARM_TYPE, blank=True)
    arm_condition = models.CharField(max_length=50, choices=Choices.CONDITION, blank=True)
    roller_condition = models.CharField(max_length=50, choices=Choices.CONDITION, blank=True)
    battery_condition = models.CharField(max_length=50, choices=Choices.CONDITION, blank=True)
    internal_activation = models.CharField(max_length=50, choices=Choices.SENSOR)
    internal_activation_condition = models.CharField(max_length=50, choices=Choices.CONDITION)
    external_activation  = models.CharField(max_length=50, choices=Choices.SENSOR)
    external_activation_condition = models.CharField(max_length=50, choices=Choices.CONDITION)
    safety_sensor = models.CharField(max_length=50, choices=Choices.SENSOR)
    safety_sensor_condition = models.CharField(max_length=50, choices=Choices.CONDITION)
    open_speed = models.IntegerField()
    close_speed = models.IntegerField()
    hold_open = models.IntegerField()
    hours = models.IntegerField()
    cycles = models.IntegerField()
    notes = models.TextField(blank=True)
    image1 = models.ImageField()
    image2 = models.ImageField(blank=True)
    image3 = models.ImageField(blank=True)
    image4 = models.ImageField(blank=True)
    image5 = models.ImageField(blank=True)
    image6 = models.ImageField(blank=True)
    status = models.CharField(max_length=50, choices=Choices.STATUS, default="Created")


class Stock(models.Model):
    qty = models.IntegerField()
    item = models.CharField(max_length=50)
    description = models.TextField()
    location = models.CharField(max_length=50, choices=Choices.stock_location)
    cost_price = models.IntegerField(default=0)
    sale_price = models.IntegerField(default=0)

