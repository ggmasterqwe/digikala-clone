from rest_framework import serializers
from .models import Product

class CreateProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['price', 'description', 'name']