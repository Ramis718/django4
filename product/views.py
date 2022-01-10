from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework  import status
from .serializers import ProductSerializer, ProductDatailSerializer
from .models import  Product

@api_view(['GET'])
def index(request):
    context = {
        'namber': 150,
        'float': 1.41,
        'text': 'Hello world',
        'list': [1, 6, 3],
        'dict': {'name': 'Azamat'}
    }    
    return Response(data=context)


@api_view(['GET'])
def product_list_view(request):
    product = Product.objects.all()
    data = ProductSerializer(product, many=True).data
    return Response(data=data)

@api_view(['GET'])
def product_datail_view(request, id):
    try:
        product= Product.objects.get(id=id)
    except Product.DoesNotExist:    
        return Response(status=status.HTTP_404_NOT_FOUND, data={'error': 'Product not found!'})
    data = ProductDatailSerializer(product, many=False).data
    return Response(data=data)