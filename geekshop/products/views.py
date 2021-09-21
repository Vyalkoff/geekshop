from pathlib import Path
from django.shortcuts import render
import json


# Create your views here.
def index(request):
    return render(request, 'products/index.html', context={'title': 'geekshop'})


def products(request):
    PATH_APP_JS = Path(__file__).resolve().parent.joinpath('fixtu', 'products.json')
    with open(PATH_APP_JS, 'r', encoding='utf-8') as f:
        js_prod = json.load(f)
    context = {
        'title': 'geekshop',
        'products': js_prod
    }

    return render(request, 'products/products.html', context=context)
