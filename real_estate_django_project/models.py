from django.db import models

class Clients(models.Model):
    name = models.CharField(max_length=30, blank=False, null=False)
    idnum = models.IntegerField(blank=False, null=False)
    address = models.CharField(max_length=30, blank=False, null=False)
    housenum = models.CharField(max_length=30, blank=False, null=False)
    contact = models.CharField(max_length=30, blank=False, null=False)
    payment = models.CharField(max_length=30, blank=False, null=False)
