from __future__ import unicode_literals
from django.db import models
from django.utils import timezone


# Create your models here.
class Locations(models.Model):
    location_name = models.CharField(max_length=45)
    location_long = models.CharField(max_length=45)
    location_lat = models.CharField(max_length=45)
    location_description = models.CharField(max_length=255, blank=True, null=True)
    nearest_town = models.CharField(max_length=45, blank=True, null=True)
    date_created = models.DateTimeField(default=timezone.now)
    last_updated = models.DateTimeField(default=timezone.now, blank=True, null=True)
    updated_by = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'locations'


class Farmers(models.Model):
    farmer_fname = models.CharField(db_column='Farmer_fName', max_length=255)  # Field name made lowercase.
    farmer_lname = models.CharField(db_column='Farmer_lName', max_length=255)  # Field name made lowercase.
    farmer_sname = models.CharField(db_column='Farmer_sName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    farmer_location = models.ForeignKey('Locations', models.DO_NOTHING)  # Field name made lowercase.
    farmer_username = models.CharField(db_column='Farmer_userName', unique=True, max_length=45)  # Field name made lowercase.
    farmer_password = models.CharField(db_column='Farmer_password', max_length=255)  # Field name made lowercase.
    date_created = models.DateTimeField(default=timezone.now)
    last_updated = models.DateTimeField(default=timezone.now, blank=True, null=True)
    updated_by = models.IntegerField(blank=True, null=True)

    # class Meta:
    #     db_table = 'farmers',
    #     ordering = ('date_created',)
