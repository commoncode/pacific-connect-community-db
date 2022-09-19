from django.db import models


class Person(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    country = models.CharField(max_length=100, blank=True)
    mobile_number = models.CharField(max_length=20, blank=True)
