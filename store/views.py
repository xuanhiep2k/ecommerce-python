from unicodedata import category
from django.shortcuts import get_object_or_404, render
from django.views.generic import ListView
from django.views.generic.detail import DetailView

from store.models import Category, Product

class ProductList(ListView):
    queryset = Product.objects.all()
    template_name = 'store/home.html'
    
class ProductDetail(DetailView):
    model = Product
    template_name = 'store/products/single.html'

class CategoryList(ListView):
    model = Category
    template_name = 'store/products/category.html'
    
    def get_queryset(self, **kwargs):
        category = super().get_queryset(**kwargs).filter(slug=self.kwargs['category_slug']).first()
        return Product.objects.filter(category=category)
    

def category_list(request, category_slug=None):
    category = get_object_or_404(Category, slug=category_slug)
    products = Product.objects.filter(category=category)
    return render(request, 'store/products/category.html', {'category': category, 'products': products})

