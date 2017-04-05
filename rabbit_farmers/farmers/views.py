from django.contrib.auth import get_user_model
from rest_framework import viewsets, authentication, filters
from rest_framework.permissions import IsAuthenticated
# from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Farmers, Locations
from .serializers import FarmersSerializer, LocationsSerializer
User = get_user_model()


class DefaultMixin(object):
    """Default settings for view authentication, permissions,
        filtering and pagination."""
    authentication_classes = (
        authentication.BasicAuthentication,
    )
    permission_classes = (IsAuthenticated,)
    # permission_classes = (IsAuthenticatedOrReadOnly,)
    paginate_by = 25
    paginate_by_param = 'page_size'
    max_paginate_by = 100
    filter_backends = (
        filters.DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    )


# class UserViewSet(DefaultMixin, viewsets.ReadOnlyModelViewSet):
#     """API endpoint for listing users."""
#     lookup_field = User.USERNAME_FIELD
#     lookup_url_kwarg = User.USERNAME_FIELD
#     queryset = User.objects.order_by(User.USERNAME_FIELD)
#     serializer_class = UserSerializer


class FarmersViewSet(DefaultMixin, viewsets.ModelViewSet):
    """API endpoint for listing and creating farmers."""
    queryset = Farmers.objects.all()
    serializer_class = FarmersSerializer


class LocationsViewSet(DefaultMixin, viewsets.ModelViewSet):
    """API endpoint for listing and creating farmers."""
    queryset = Locations.objects.all()
    serializer_class = LocationsSerializer

