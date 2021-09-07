from django.urls import path
from .views import ProductListAPIView, ProductAPIRUDView

app_name = 'storeapi'
urlpatterns=[
    path('', ProductListAPIView.as_view(), name='product-list'),
    path('<slug:slug>/', ProductAPIRUDView.as_view(), name='product-rud'),
]