import datetime

from django.db import models


class Person(models.Model):
    name = models.CharField(max_lenght=100)
    phone = models.CharField(blank=True, max_length=100)
    description = models.CharField(blank=True, max_length=100)
    create_date = models.DateTimeField("date create")

    def __str__(self):
        return self.name

class Car(models.Model):
    vin = models.CharField(blank=True, max_length=100)
    reg_num = models.CharField(blank=True, max_length=100)
    model = models.CharField(blank=True, max_length=100)
    brand = models.CharField(blank=True, max_length=100)
    person_name = models.ForeignKey(Person, on_delete=models.PROTECT)
