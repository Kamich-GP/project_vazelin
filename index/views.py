from django.shortcuts import render, redirect
from .models import Category, Product
from .forms import RegForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout
from django.views import View


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


# Поиска товара по названию
def search_product(request):
    if request.method == 'POST':
        get_product = request.POST.get('search_product')
        searched_product = Product.objects.filter(product_name__iregex=get_product)

        if searched_product:
            context = {
                'products': searched_product,
                'request': get_product
            }
            return render(request, 'result.html', context=context)
        else:
            context = {
                'products': '',
                'request': get_product
            }
            return render(request, 'result.html', context=context)


# Регистрация
class Register(View):
    template_name = 'registration/register.html'


    def get(self, request):
        context = {'form': RegForm}
        return render(request, self.template_name, context=context)


    def post(self, request):
        form = RegForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password2')

            user = User.objects.create_user(username=username,
                                            email=email,
                                            password=password)
            user.save()
            login(request, user)
            return redirect('/')
