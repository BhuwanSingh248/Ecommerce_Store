from django.shortcuts import get_object_or_404, render
from django.http import JsonResponse
from .basket import Basket
from apps.Store.models import Product

def basket_summary(request):
    return render(request, 'Store/basket/summary.html')

def basket_add(request):
    basket = Basket(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('productid'))
        product_qty = int(request.POST.get('productqty'))
        product = get_object_or_404(Product, id = product_id)
        basket.add(product=product, qty=product_qty)
        basket_qty = basket.__len__()
        response = JsonResponse({
            'qty':basket_qty  
        })
        return response
