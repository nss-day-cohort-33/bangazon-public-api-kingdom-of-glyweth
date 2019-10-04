"""View module for handling requests about order products"""

from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from bangazon.models import Order_Products, Product, Order


class Order_Products_Serializer(serializers.HyperlinkedModelSerializer):
    """JSON serializer for order products

    Arguments:
        serializers
    """
    class Meta:
        model = Order_Products
        url = serializers.HyperlinkedIdentityField(
            view_name='order_product',
            lookup_field='id'
        )
        fields = ('id', 'product_id', 'order_id', 'review')
        
        
class Order_Products_2(ViewSet):
    """order products for bangazon"""
    
    def create(self, request):
        """Handle POST operations

        Returns:
            Response -- JSON serialized Order_Products instance
        """
        new_order_product = Order_Products()
        new_order_product.review = request.data['review']
        
        product = Product.get(pk=request.data['product_id'])
        new_order_product.product = product
        order = Order.get(pk=request.data['order_id'])
        new_order_product.order = order
        new_order_product.save()
        
        serializer = Order_Products_Serializer(new_order_product, context={'request': request})
        
        return Response(serializer.data)
    
    def retrieve(self, request, pk=None):
        """Handle GET requests for single order product

        Returns:
            Response -- JSON serialized order product instance
        """
        try:
            area = Order_Products.objects.get(pk=pk)
            serializer = Order_Products_Serializer(
                area, context={'request': request}
            )
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)
        
    def update(self, request, pk=None):
        """Handle PUT requests for an order product

        Returns:
            Response -- Empty body with 204 status code
        """
        order_product = Order_Products.objects.get(pk=pk)
        product = Product.objects.get(pk=request.data['product_id'])
        order = Order.objects.get(pk=request.data['order_id'])
        order_product.review = request.data['review']
        order_product.product = product
        order_product.order = order
        order_product.save()
        
        return Response({}, status=status.HTTP_204_NO_CONTENT)
    
    def destroy(self, request, pk=None):
        """Handle DELETE requests for a single order product

        Returns:
            Response -- 200, 404, or 500 status code
        """
        try:
            Order_Products.objects.get(pk=pk).delete()
            
            return Response({}, status=status.HTTP_204_NO_CONTENT)
        
        except Order_Products.DoesNotExist as ex:
             return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

        except Exception as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
    def list(self, request):
        """Handle GET requests to park areas resource

        Returns:
            Response -- JSON serialized list of park areas
        """
        order_products = Order_Products.objects.all()
        serializer = Order_Products_Serializer(
            order_products, many=True, context={'request': request}
        )
        return Response(serializer.data)
        