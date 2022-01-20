from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework  import status
from .serializers import ProductSerializer, ProductDatailSerializer, ReviewSerializer, TagSerializer, ProductCreateSerializer
from .models import  Product
from distutils import errors

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


@api_view(['GET', 'POST'])
def product_list_view(request):
    if request.method == 'GET':
        product = Product.objects.all()
        data = ProductSerializer(product, many=True).data
        return Response(data=data)
    elif request.method == 'POST':
        print('request.data-', request.data)
        serializer = ProductCreateSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(status=status.HTTP_406_Not_ACCEPTABLE, data={'errors': serializer.errors})
        print('validated-', serializer.validated.data)    
        name = serializer.validated_data['name']
        description = serializer.validated_data.get('description', '')
        duration = serializer.validated_data['duration']
        is_active = serializer.validated_data['is_active']
        tag = serializer.validated_data['tag']
        product = Product.objects.create(
            name=name, description=description, duration=duration, is_active=is_active)
        
        product.tag.set(tag)

        return Response(data=ProductSerializer(product).data, status=status.HTTP_201_CREATED)
        
@api_view(['GET', 'DELETE'])
def product_datail_view(request, id):
    try:
        product= Product.objects.get(id=id)
    except Product.DoesNotExist:    
        return Response(status=status.HTTP_404_NOT_FOUND, data={'error': 'Product not found!'})
    if request.method == 'GET':
        data = ProductDatailSerializer(product, many=False).data
        return Response(data=data)
    elif request.method == 'DELETE':
        product.delete()    
        return Response(data={'message': 'delete product'})