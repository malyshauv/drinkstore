from rest_framework import serializers
from .models import Product, Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name', 'slug')

class ProductSerializer(serializers.ModelSerializer):
    category_name = serializers.ReadOnlyField(source = 'category.name')
    class Meta:
        model = Product
        fields = (
            'id', 'category', 'category_name', 'name', 
            'description', 'price', 'image', 'is_enabled'
        )
        