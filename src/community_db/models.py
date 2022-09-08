from django.db import models


class Person(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100, blank=True)
    country = models.CharField(max_length=100, blank=True)
    mobile_number = models.CharField(max_length=20, blank=True)

    # another change, but on a different branch <- this change was made on `my-branch`
    # now this change is being made on `my-branch-inner-1`