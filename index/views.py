from django.shortcuts import render
from .models import Category, Product


# Create your views here.
def home_page(request):
    products = Product.objects.all()
    categories = Category.objects.all()
    context = {
        'products': products,
        'categories': categories
    }
    return render(request, 'home.html', context)
