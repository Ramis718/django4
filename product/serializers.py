from rest_framework import serializers
from .models import Product, Review, Tag


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