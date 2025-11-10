from rest_framework import serializers
from .models import Order, OrderItem, AdminNote
from products.serializers import ProductSerializer


class OrderItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)

    class Meta:
        model = OrderItem
        fields = ['id', 'product', 'product_name', 'quantity', 'price']


class AdminNoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdminNote
        fields = ['id', 'note', 'created_at']
        read_only_fields = ['created_at']


class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True, read_only=True)
    admin_notes = AdminNoteSerializer(many=True, read_only=True)
    user_email = serializers.EmailField(source='user.email', read_only=True)

    class Meta:
        model = Order
        fields = ['id', 'order_id', 'user', 'user_email', 'total_amount', 'status', 'shipping_address', 'items', 'admin_notes', 'created_at', 'updated_at']
        read_only_fields = ['id', 'order_id', 'created_at', 'updated_at']


class OrderCreateSerializer(serializers.Serializer):
    items = serializers.ListField(child=serializers.DictField())
    shipping_address = serializers.DictField()

    def validate_items(self, value):
        if not value:
            raise serializers.ValidationError("Items cannot be empty")
        return value

    def validate_shipping_address(self, value):
        required_fields = ['full_name', 'address', 'city', 'postal_code', 'country', 'phone']
        for field in required_fields:
            if field not in value:
                raise serializers.ValidationError(f"{field} is required")
        return value
