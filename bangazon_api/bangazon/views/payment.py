"""View module for handling requests about Customer Payment Methods"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from ..models import Payment, Customer


class PaymentSerializer(serializers.HyperlinkedModelSerializer):
    """JSON serializer for Payment

    Arguments:
        serializers
    """
    class Meta:
        model = Payment
        url = serializers.HyperlinkedIdentityField(
            view_name='payment',
            lookup_field='id'
        )
        fields = ('id', 'url', 'merchant_name', 'account_number', 'creation_date', 'expiration_date', 'customer_id')


class Payments(ViewSet):
    """Customer Payment Methods for Bangazon"""

    def create(self, request):
        """Handle POST operations

        Returns:
            Response -- JSON serialized Payment instance
        """
        new_payment = Payment()
        new_payment.merchant_name = request.data["merchant_name"]
        new_payment.account_number = request.data["account_number"]
        new_payment.expiration_date = request.data["expiration_date"]

        customer = Customer.objects.get(user=request.auth.user)
        new_payment.customer = customer
        new_payment.save()

        serializer = PaymentSerializer(new_payment, context={'request': request})

        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        """Handle GET requests for single customer payment method

        Returns:
            Response -- JSON serialized customer instance
        """
        try:
            payment = Payment.objects.get(pk=pk)
            serializer = PaymentSerializer(payment, context={'request': request})
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)

    def update(self, request, pk=None):
        """Handle PUT requests for a customer payment method

        Returns:
            Response -- Empty body with 204 status code
        """
        payment = Payment.objects.get(pk=pk)
        customer = Customer.objects.get(pk=request.data["customer_id"])
        payment.merchant_name = request.data["merchant_name"]
        payment.account_number = request.data["account_number"]
        payment.creation_date = request.data["creation_date"]
        payment.expiration_date = request.data["expiration_date"]
        payment.customer = customer
        payment.save()

        return Response({}, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk=None):
        """Handle DELETE requests for a single customer payment method

        Returns:
            Response -- 200, 404, or 500 status code
        """
        try:
            this_payment = Payment.objects.get(pk=pk)
            this_payment.delete()

            return Response({}, status=status.HTTP_204_NO_CONTENT)

        except Payment.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

        except Exception as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def list(self, request):
        """Handle GET requests to customer payment resource

        Returns:
            Response -- JSON serialized list of park attractions
        """

        payments = Payment.objects.all()
        payment = self.request.query_params.get('customer', None)
        current_user = Customer.objects.get(user=request.auth.user)

        if payment == "current":
            payments = payments.filter(customer=current_user)

        serializer = PaymentSerializer(
            payments, many=True, context={'request': request})
        return Response(serializer.data)

