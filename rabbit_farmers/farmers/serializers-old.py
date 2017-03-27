from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Farmers, Locations


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')


class FarmersSerializer(serializers.ModelSerializer):
    farmer_location = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Farmers
        fields = ('id', 'farmer_fname', 'farmer_lname', 'farmer_location', 'farmer_password',
                  'date_created', 'farmer_username')


class LocationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Locations
        fields = ('id', 'location_name', 'location_long', 'location_lat', 'location_description',
                  'date_created')
