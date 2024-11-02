from rest_framework import serializers
from .models import Product
from django.contrib.auth.models import User

class ProductSerializer(serializers.ModelSerializer):
    seller = serializers.PrimaryKeyRelatedField(read_only=True)
    buyer = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'price', 'seller', 'buyer', 'is_seller_anonymous', 'is_buyer_anonymous', 'is_sold', 'created_at']
        read_only_fields = ['is_sold', 'buyer', 'created_at']

    def create(self, validated_data):
        validated_data['seller'] = self.context['request'].user
        return super().create(validated_data)

class PurchaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id']

    def update(self, instance, validated_data):
        instance.is_sold = True
        instance.buyer = self.context['request'].user
        instance.save()
        return instance
