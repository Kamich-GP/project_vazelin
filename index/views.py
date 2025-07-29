from django.shortcuts import render
from .models import Category, Product


# Create your views here.
# Главная страница
def home_page(request):
    products = Product.objects.all()
    categories = Category.objects.all()
    context = {
        'products': products,
        'categories': categories
    }
    return render(request, 'home.html', context)


# Страница с товарами по категории
def category_page(request, pk):
    category = Category.objects.get(id=pk)
    products = Product.objects.filter(product_category=category)
    context = {
        'category': category,
        'products': products
    }
    return render(request, 'category.html', context)


# Страница с определенным товаром
def product_page(request, pk):
    product = Product.objects.get(id=pk)
    context = {
        'product': product
    }
    return render(request, 'product.html', context)
