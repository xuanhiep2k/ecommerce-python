
from django.urls import path
from .views import CategoryList, ProductDetail, ProductList
from . import views

app_name = 'store'

urlpatterns = [
    path('', ProductList.as_view(), name='product_list'),
    path('<slug:slug>', ProductDetail.as_view(), name='product_detail'),
    path('shop/<slug:category_slug>/', CategoryList.as_view(), name='category_list'),
]