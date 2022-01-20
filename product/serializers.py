from rest_framework import serializers
from .models import Product, Review, Tag
from rest_framework.exceptions import ValidationError



class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields ='__all__'

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = 'id text'.split()    

class ProductSerializer(serializers.ModelSerializer):
    tag = serializers.SerializerMethodField()
    reviews = serializers.SerializerMethodField()
    class Meta:
        model = Product
        # fields = '__all__'
        fields =[ 'id', 'name', 'tag', 'reviews', 'cout_tag', 'review']

    def get_reviews(self, product):
        rot = Review.objects.filter(product=product, value__gt=5)    
        data = ReviewSerializer(rot, many=True).data

    def get_tag(self, product):
        return TagSerializer(product.tag.filter(is_active=True), many=True).data    

class ProductDatailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        # fields = '__all__'
        fields = ['id name', 'description', 'category', 'cout_tag']       


class TagCreateSerializer(serializers.Serializer):
    name= serializers.CharField()
    is_active = serializers.BooleanField()

class ProductCreateSerializer(serializers.Serializer):
    name = serializers.CharField(min_length=4, max_length=60)
    description = serializers.CharField(required=False)
    duration = serializers.IntegerField(default=1)
    is_active = serializers.BooleanField()
    tag = serializers.ListField(child=serializers.IntegerField()) 

    def validate_description(self, name):
        movies = Movie.objects.filter(name=name)
        if movies:
            raise ValidationError('Movie already ') 
        return description           