import json
from django.http import HttpResponseServerError
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authtoken.models import Token
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from bangazon.models import Customer

class customer_serializer(serializers.HyperlinkedModelSerializer):
    """ JSON Serializer for Customers"""

    class Meta:
        model = Customer
        url = serializers.HyperlinkedIdentityField(
            view_name='customer',
            lookup_field='id'
        )
        fields = ('id','phone_number', 'address', 'city')
        depth = 1

class Customers(ViewSet):
    """Customers for the bangazon app"""

    """Create customer is accomplished in register view"""

    def create(self, request):
        """Handles Post Operations - Ben"""

        new_customer = Customer()
        new_customer.phone_number = request.data["phone_number"]
        new_customer.address = request.data["address"]
        new_customer.city = request.data["city"]
        new_customer.save()

        serializer = customer_serializer(new_customer, context={'request': request})

        return Response(serializer.data)


    def retrieve(self, request, pk=None):
        """ Handles get request for a single customer for the profile page - Ben"""

        try:
            customer = Customer.objects.get(pk=pk)
            serializer = customer_serializer(customer, context = {'request': request})
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)

    def update(self, request, pk=None):
        """Handles put request for the Customer on their proile - Ben"""

        customer = Customer.objects.get(pk)
        customer.phone_number = request.data["phone_number"]
        customer.address = request.data["address"]
        customer.city = request.data["city"]
        customer.save()

        return Response({}, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk=None):
        """Handles the delete request request for the Customer on their profile - Ben"""
        try:
            customer = Customer.objects.get(pk)
            customer.delete()

            return Response({}, status=status.HTTP_204_NO_CONTENT)

        except Customer.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

        except Exception as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def list(self, request):
        """Handles the get all request for the customers - Ben"""

        user = Customer.objects.get(user=request.auth.user)
        customer = Customer.objects.filter(user)
        serializer = customer_serializer(
            customer, many=True, context={'request': request}
        )
        return Response(serializer.data)