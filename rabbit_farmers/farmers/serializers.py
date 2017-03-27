from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import Farmers, Locations
from rest_framework.reverse import reverse


User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    full_name = serializers.CharField(source='get_full_name', read_only=True)

    class Meta:
        model = User
        fields = ('id', User.USERNAME_FIELD, 'full_name', 'is_active')


class FarmersSerializer(serializers.ModelSerializer):

    # loc = serializers.HyperlinkedRelatedField(many=True, view_name='locations-detail')

    class Meta:
        model = Farmers
        fields = ('id', 'farmer_fname', 'farmer_lname', 'farmer_location', 'farmer_password',
                  'date_created', 'farmer_username', 'date_created')

    def get_links(self, obj):
        request = self.context['request']
        return {
            'self': reverse('farmer-details', kwargs={'pk': obj.pk}, request=request),
        }


class LocationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Locations
        fields = ('id', 'location_name', 'location_lat', 'location_long', 'location_description',
                  'nearest_town')
