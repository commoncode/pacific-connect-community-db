from django.db import models


class Person(models.Model):
    class Colours(models.TextChoices):
        RED = ('red', 'red')
        BLUE = ('blue', 'blue')
    
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100, blank=True)
    country = models.CharField(max_length=100, blank=True)
    mobile_number = models.CharField(max_length=20, blank=True)
    email_address = models.EmailField(max_length=800, blank=True)
    favourite_colour = models.CharField(max_length=50, choices=Colours.choices, default=Colours.RED.value)