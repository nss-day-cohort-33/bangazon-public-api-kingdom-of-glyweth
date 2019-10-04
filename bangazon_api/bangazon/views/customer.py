import json
from django.http import HttpResponse
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

@csrf_exempt
def login_user(request):
    '''Handles the authentication of a user

    Method arguments:
      request -- The full HTTP request object
    '''

    req_body = json.loads(request.body.decode())

    # If the request is a HTTP POST, try to pull out the relevant information.
    if request.method == 'POST':

        # Use the built-in authenticate method to verify
        username = req_body['username']
        password = req_body['password']
        authenticated_user = authenticate(username=username, password=password)

        # If authentication was successful, respond with their token
        if authenticated_user is not None:
            token = Token.objects.get(user=authenticated_user)
            data = json.dumps({"valid": True, "token": token.key})
            return HttpResponse(data, content_type='application/json')

        else:
            # Bad login details were provided. So we can't log the user in.
            data = json.dumps({"valid": False})
            return HttpResponse(data, content_type='application/json')
            
@csrf_exempt
def register_user(request):
    '''Handles the creation of a new user for authentication

    Method arguments:
      request -- The full HTTP request object
    '''

    # Load the JSON string of the request body into a dict
    req_body = json.loads(request.body.decode())

    # Create a new user by invoking the `create_user` helper method
    # on Django's built-in User model
    new_user = User.objects.create_user(
        username=req_body['username'],
        email=req_body['email'],
        password=req_body['password'],
        first_name=req_body['first_name'],
        last_name=req_body['last_name']
    )

    customer = Customer.objects.create(
        family_members=req_body['family_members'],
        user=new_user
    )

    # Commit the user to the database by saving it
    customer.save()

    # Use the REST Framework's token generator on the new user account
    token = Token.objects.create(user=new_user)

    # Return the token to the client
    data = json.dumps({"token": token.key})
    return HttpResponse(data, content_type='application/json')


class Customers(ViewSet):
    """Customers for the bangazon app"""

    def create(self, request):
        """Handles Post Operations - Ben"""

        new_customer = Customer()
        new_customer.first_name = request.data("first_name")
        new_customer.last_name = request.data("last_name")
        new_customer.email = request.data("email")
        new_customer.phone_number = request.data("phone_number")
        new_customer.address = request.data("address")
        new_customer.city = request.data("city")
        new_customer.signup_date = request.data("signup_date")
        new_customer.is_active = True
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
        customer.first_name = request.data("first_name")
        customer.last_name = request.data("last_name")
        customer.email = request.data("email")
        customer.phone_number = request.data("phone_number")
        customer.address = request.data("address")
        customer.city = request.data("city")
        customer.signup_date = request.data("signup_date")
        customer.is_active = True
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

        customer = Customer.objects.all()
        serializer = customer_serializer(
            customer, many=True, context={'request': request}
        )
        return Response(serializer.data)