from django.shortcuts import render
from .models import ProductCategory, Product


# Create your views here.
def index(request):
    return render(request, 'products/index.html', context={'title': 'geekshop'})


def products(request, category_id=None):
    product = Product.objects.filter(category_id=category_id) if category_id is not None else Product.objects.all()
    context = {
        'title': 'geekshop',
        'products': product,
        'category_products': ProductCategory.objects.all(),

    }

    return render(request, 'products/products.html', context=context)
