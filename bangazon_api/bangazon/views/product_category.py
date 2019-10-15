"""View module for handling requests about product category"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from bangazon.models import Product_Category

class Product_Category_Serializer(serializers.HyperlinkedModelSerializer):
    """JSON serializer for product category

    Arguments:
        serializers
    """
    class Meta:
        model = Product_Category
        url = serializers.HyperlinkedIdentityField(
            view_name='product_category',
            lookup_field='id'
        )
        fields = ('id', 'name')

class Product_Categories(ViewSet):
    """Product categories for Bangazon"""

    def create(self, request):
        """Handle POST operations

        Returns:
            Response -- JSON serialized product_category instance
        """
        new_category = Product_Category()
        new_category.name = request.data["name"]
        new_category.save()

        serializer = Product_Category_Serializer(new_category, context={'request': request})

        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        """Handle GET requests for single category

        Returns:
            Response -- JSON serialized category instance
        """
        try:
            category = Product_Category.objects.get(pk=pk)
            serializer = Product_Category_Serializer(category, context={'request': request})
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)

    def update(self, request, pk=None):
        """Handle PUT requests for an category

        Returns:
            Response -- Empty body with 204 status code
        """
        new_category = Product_Category.objects.get(pk=pk)
        new_category.name = request.data["name"]
        new_category.save()

        return Response({}, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk=None):
        """Handle DELETE requests for a single category

        Returns:
            Response -- 200, 404, or 500 status code
        """
        try:
            category = Product_Category.objects.get(pk=pk)
            category.delete()

            return Response({}, status=status.HTTP_204_NO_CONTENT)

        except Product_Category.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

        except Exception as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def list(self, request):
        """Handle GET requests to product category resource

        Returns:
            Response -- JSON serialized list of orders
        """
        category = Product_Category.objects.all()

       

        serializer = Product_Category_Serializer(
            category, many=True, context={'request': request})
        return Response(serializer.data)

