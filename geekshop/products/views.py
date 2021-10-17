from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render
from .models import ProductCategory, Product


# Create your views here.
def index(request):
    return render(request, 'products/index.html', context={'title': 'geekshop'})


def products(request, category_id=None, page_id=1):
    product = Product.objects.filter(category_id=category_id) if category_id is not None else Product.objects.all()
    paginator = Paginator(product, per_page=3)
    try:
        products_paginator = paginator.page(page_id)
    except PageNotAnInteger:
        products_paginator = paginator.page(1)
    except EmptyPage:
        products_paginator = paginator.page(paginator.num_pages)

    context = {
        'title': 'Каталог',
        'category_products': ProductCategory.objects.all(),
        'products': products_paginator,
    }

    return render(request, 'products/products.html', context=context)
