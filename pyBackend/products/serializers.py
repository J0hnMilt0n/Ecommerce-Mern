from rest_framework import serializers
from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'slug', 'description', 'price', 'category', 'weight', 'stock', 'images', 'is_deleted', 'created_at', 'updated_at']
        read_only_fields = ['id', 'slug', 'created_at', 'updated_at']

    def validate_images(self, value):
        if not isinstance(value, list):
            raise serializers.ValidationError("Images must be a list")
        return value
