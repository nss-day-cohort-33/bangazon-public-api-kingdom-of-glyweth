from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from ..models import Product, Customer, Product_Category


class Product_Serializer(serializers.HyperlinkedModelSerializer):
    """JSON serializer for bangazon products
    Arguments:
        serializers
    """
    class Meta:
        model = Product
        url = serializers.HyperlinkedIdentityField(
            view_name='product',
            lookup_field='id'
        )
        fields = ('id', 'url', 'name', 'customer', 'customer_id', 'price', 'description', 'product_category_id',
                  'quantity_available', 'quantity_sold', 'date_created', 'image' )
        # depth = 1


class Products(ViewSet):
    """Products for Bangazon Api"""

    def create(self, request):
        """Handle POST operations
        Returns:
            Response -- JSON serialized Product instance
        """
        new_product = Product()
        customer = Customer.objects.get(user=request.auth.user)
        product_category = Product_Category.objects.get(
            pk=request.data['product_category_id'])

        new_product.customer = customer
        new_product.product_category = product_category
        new_product.name = request.data["name"]
        new_product.price = request.data["price"]
        new_product.description = request.data["description"]
        new_product.quantity_available = request.data["quantity_available"]
        new_product.quantity_sold = request.data["quantity_sold"]
        # new_product.image = request.data.get["image", None]
        new_product.save()

        serializer = Product_Serializer(
            new_product, context={'request': request})
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        """Handle GET requests for a single product
        Returns:
            Response -- JSON serialized product instance
        """
        try:
            product = Product.objects.get(pk=pk)
            serializer = Product_Serializer(
                product, context={'request': request})
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)

    def update(self, request, pk=None):
        """Handle PUT requests for an individual product
        Returns:
            Response -- Empty body with 204 status code
        """
        new_product = Product.objects.get(pk=pk)
        new_product.name = request.data["name"]
        customer = Customer.objects.get(pk=request.data['customer_id'])
        new_product.customer = customer
        new_product.price = request.data["price"]
        new_product.description = request.data["description"]
        product_category = Product_Category.objects.get(
            pk=request.data['product_category_id'])
        new_product.product_category = product_category
        new_product.quantity_available = request.data["quantity_available"]
        new_product.quantity_sold = request.data["quantity_sold"]
        new_product.date_created = request.data["date_created"]
        new_product.image = request.data["image"]
        new_product.save()

        return Response({}, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk=None):
        """Handle DELETE requests for a single product
        Returns:
            Response -- 200, 404, or 500 status code
        """
        try:
            new_product = Product.objects.get(pk=pk)
            new_product.delete()

            return Response({}, status=status.HTTP_204_NO_CONTENT)

        except Product.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

        except Exception as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def list(self, request):
        """Handle GET requests to product resource
        Returns:
            Response -- JSON serializer list of products
        """
        products = Product.objects.all()
        product_list = []

        product_category = self.request.query_params.get(
            'product_category', None)
        if product_category is not None:
            products = products.filter(product_category__id=product_category)

        user = self.request.query_params.get(
            'user', None)
        if user is not None:
            current_user = Customer.objects.get(user=request.auth.user)
            products = products.filter(customer=current_user)

        category = self.request.query_params.get('category', None)
        quantity_available = self.request.query_params.get('quantity_available', None)
        if category is not None:
            products = products.filter(product_category__id=category)
            for product in products:
                if product.quantity_available > 0:
                    product_list.append(product)
            products = product_list
            

        if quantity_available is not None:
            quantity_available = int(quantity_available)
            length = len(products)
            new_products = list()
            count = 0
            for product in products:
                count += 1
                if count - 1 + quantity_available >= length:
                    new_products.append(product)
                    if count == length:
                        products = new_products
                        break
                    
        products = products.reverse()
        quantity = self.request.query_params.get('quantity', None)
        if quantity is not None:
            products = products[:int(quantity)]
        

        serializer = Product_Serializer(
            products, many=True, context={'request': request})
        return Response(serializer.data)
