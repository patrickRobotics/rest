from __future__ import unicode_literals
from django.db import models
from django.utils import timezone


class Locations(models.Model):
    location_name = models.CharField(max_length=45)
    location_long = models.CharField(max_length=45)
    location_lat = models.CharField(max_length=45)
    location_description = models.CharField(max_length=255, blank=True,
                                            null=True)
    nearest_town = models.CharField(max_length=45, blank=True, null=True)
    date_created = models.DateTimeField(default=timezone.now)
    last_updated = models.DateTimeField(default=timezone.now, blank=True,
                                        null=True)
    updated_by = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'locations'

    def __str__(self):
        return self.location_name


class Farmers(models.Model):
    farmer_fname = models.CharField(db_column='Farmer_fName',
                                    max_length=255)
    farmer_lname = models.CharField(db_column='Farmer_lName',
                                    max_length=255)
    farmer_sname = models.CharField(db_column='Farmer_sName', max_length=255,
                                    blank=True, null=True)
    farmer_location = models.ForeignKey('Locations', models.DO_NOTHING,
                                        related_name='locations')
    farmer_username = models.CharField(db_column='Farmer_userName',
                                       unique=True, max_length=45)
    farmer_password = models.CharField(db_column='Farmer_password',
                                       max_length=255)
    date_created = models.DateTimeField(default=timezone.now)
    last_updated = models.DateTimeField(default=timezone.now,
                                        blank=True, null=True)
    updated_by = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.farmer_username

