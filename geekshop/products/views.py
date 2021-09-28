from django.shortcuts import render
from .models import ProductCategory, Product


# Create your views here.
def index(request):
    return render(request, 'products/index.html', context={'title': 'geekshop'})


def products(request):
    context = {
        'title': 'geekshop',
        'products': Product.objects.all(),
        'category_products': ProductCategory.objects.all(),

    }

    return render(request, 'products/products.html', context=context)
