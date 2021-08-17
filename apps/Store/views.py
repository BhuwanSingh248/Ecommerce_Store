from django.shortcuts import get_object_or_404, render

# Create your views here.
from .models import Category, Product


def category_list(request, category_slug=None):
    category = get_object_or_404(Category, slug=category_slug)
    products = Product.objects.filter(category=category)
    return render(request, 'Store/products/category.html', {'category': category, 'products': products})
    
def product_all(request):
    products = Product.objects.all()
    return render(request, 'Store/home.html',{'products':products})

def product_detail(request, slug):
    product = get_object_or_404(Product, slug = slug, in_stock=True)
    return render(request, 'Store/products/detail.html', {'product':product})
