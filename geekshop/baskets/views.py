from django.http import JsonResponse
from django.shortcuts import render
from django.shortcuts import HttpResponseRedirect
from django.template.loader import render_to_string

from products.models import Product
from baskets.models import Basket
# Create your views here.
from django.contrib.auth.decorators import login_required


@login_required
def basket_add(request, product_id):
    user_select = request.user
    product = Product.objects.get(id=product_id)
    baskets = Basket.objects.filter(user=user_select, product=product)
    if not baskets.exists():
        Basket.objects.create(user=user_select, product=product, quantity=1)
    else:
        basket = baskets.first()
        basket.quantity += 1
        basket.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def basket_remove(request, product_id):
    Basket.objects.get(id=product_id).delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@login_required
def basket_edit(request, id, quantity):
    if request.is_ajax():
        basket = Basket.objects.get(id=id)
        if quantity > 0:
            basket.quantity = quantity
            basket.save()
        else:
            basket.delete()
        total_quantity = 0
        total_sum = 0
        baskets = Basket.objects.filter(user=request.user)
        for basket in baskets:
            total_quantity += basket.quantity
            total_sum += basket.sum()
        context = {
            'baskets': baskets,
            'total_quantity': total_quantity,
            'total_sum': total_sum
        }
        result = render_to_string('baskets/baskets.html', context)
        return JsonResponse({'result': result})
