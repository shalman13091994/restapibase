from rest_framework import generics, mixins, serializers
from .serializers import ProductListSerialiser
from store.models import Product


class ProductListAPIView(mixins.CreateModelMixin, generics.ListAPIView):
    serializer_class = ProductListSerialiser

    def get_queryset(self):
        return Product.objects.all()
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    


class ProductAPIRUDView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field='slug'
    serializer_class = ProductListSerialiser

    def get_queryset(self):
        return Product.objects.all()
    
    def patch(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)