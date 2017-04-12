from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import Farmers, Locations


User = get_user_model()


class UserSerializer(serializers.HyperlinkedModelSerializer):
    full_name = serializers.CharField(source='get_full_name', read_only=True)

    class Meta:
        model = User
        fields = ('id', User.USERNAME_FIELD, 'full_name', 'is_active',
                  'groups')


# class LocationsSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Locations
#         fields = ('id', 'location_name', 'location_lat', 'location_long',
#                   'location_description', 'nearest_town')


# class FarmersSerializer(serializers.ModelSerializer):
#
#     class Meta:
#         model = Farmers
#         fields = ('id', 'farmer_fname', 'farmer_lname', 'farmer_location',
#                   'farmer_password', 'date_created', 'farmer_username',
#                   'date_created')
#
#     def get_links(self, obj):
#         request = self.context['request']
#         return {
#             'self': reverse('farmer-details', kwargs={'pk': obj.pk},
#                             request=request),
#         }

class LocationsSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Locations
        fields = ('url', 'location_name', 'location_lat', 'location_long',
                  'location_description', 'nearest_town')


class FarmersSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Farmers
        fields = ('url', 'farmer_fname', 'farmer_lname', 'farmer_password',
                  'date_created', 'farmer_username', 'farmer_location',
                  'date_created')
