from .models import Farmers, Locations
from .serializers import FarmersSerializer, LocationsSerializer
from django.http import Http404
from rest_framework.reverse import reverse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status


# @api_view(['GET'])
# def api_root(request, format=None):
#     return Response({
#         'farmers': reverse('FarmersList', request=request, format=format),
#         'locations': reverse('LocationsList', request=request, format=format)
#     })


class FarmersList(APIView):
    """
    List all farmers, or create a new farmer instance.
    """
    def get(self, request, format=None):
        farmers = Farmers.objects.all()
        serializer = FarmersSerializer(farmers, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = FarmersSerializer(data=request.data)
        # import pdb
        # pdb.set_trace()
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class FarmersDetail(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    def get_object(self, pk):
        try:
            return Farmers.objects.get(pk=pk)
        except Farmers.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        farmers = self.get_object(pk)
        serializer = FarmersSerializer(farmers)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        farmers = self.get_object(pk)
        serializer = FarmersSerializer(farmers, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        farmers = self.get_object(pk)
        farmers.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class LocationsList(APIView):
    """
    List all farmers, or create a new farmer instance.
    """
    def get(self, request, format=None):
        locations = Locations.objects.all()
        serializer = LocationsSerializer(locations, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = LocationsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LocationsDetail(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    def get_object(self, pk):
        try:
            return Locations.objects.get(pk=pk)
        except Locations.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        locations = self.get_object(pk)
        serializer = LocationsSerializer(locations)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        locations = self.get_object(pk)
        serializer = LocationsSerializer(locations, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        locations = self.get_object(pk)
        locations.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

