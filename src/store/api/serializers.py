from store.models import Product
from rest_framework import serializers

class ProductListSerialiser(serializers.ModelSerializer):
    class Meta:
        model=Product
        fields='__all__'
        
    