"""View module for handling requests about orders"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from bangazon.models import Order, Customer, Payment, Order_Products, Product
from .order_product import Order_Products_Serializer

class Order_Serializer(serializers.HyperlinkedModelSerializer):
    """JSON serializer for orders

    Arguments:
        serializers
    """
    class Meta:
        model = Order
        url = serializers.HyperlinkedIdentityField(
            view_name='order',
            lookup_field='id'
        )
        fields = ('id', 'customer_id', 'payment_id', 'order_placed_date')

class Orders(ViewSet):
    """Orders for Bangazon"""

    def create(self, request):
        """Handle POST operations

        Returns:
            Response -- JSON serialized Order instance
        """
        order_item = Order_Products()
        order_item.product = Product.objects.get(pk=request.data["product_id"])

        current_customer = Customer.objects.get(user=request.auth.user)
        order = Order.objects.filter(customer=current_customer, payment=None)

        if order.exists():
            order_item.order = order[0]
        else:
            new_order = Order()
            new_order.customer = current_customer
            new_order.save()
            order_item.order = new_order

        order_item.save()

        serializer = Order_Products_Serializer(order_item, context={'request': request})

        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        """Handle GET requests for single order

        Returns:
            Response -- JSON serialized order instance
        """
        try:
            order = Order.objects.get(pk=pk)
            serializer = Order_Serializer(order, context={'request': request})
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)

    def update(self, request, pk=None):
        """Handle PUT requests for an order

        Returns:
            Response -- Empty body with 204 status code
        """
        new_order = Order.objects.get(pk=pk)
        new_order.order_placed_date = request.data["order_placed_date"]
        payment = Payment.objects.get(pk=request.data["payment_id"])
        new_order.payment = payment
        customer = Customer.objects.get(pk=request.data["customer_id"])
        new_order.customer = customer
        new_order.save()

        return Response({}, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk=None):
        """Handle DELETE requests for a single order

        Returns:
            Response -- 200, 404, or 500 status code
        """
        try:
            order = Order.objects.get(pk=pk)
            order.delete()

            return Response({}, status=status.HTTP_204_NO_CONTENT)

        except Order.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

        except Exception as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def list(self, request):
        """Handle GET requests to order resource

        Returns:
            Response -- JSON serialized list of orders
        """
        order = Order.objects.all()

        # Support filtering attractions by area id
        # area = self.request.query_params.get('area', None)
        # if area is not None:
        #     attractions = attractions.filter(area__id=area)

        serializer = Order_Serializer(
            order, many=True, context={'request': request})
        return Response(serializer.data)

