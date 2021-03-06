from django.shortcuts import render

from basketapp.models import Basket
from mainapp.models import Product


def index(request):
    title = 'магазин'

    products = Product.objects.filter(is_deleted=False, category__is_deleted=False)[:5]

    context = {
        'title': title,
        'products': products,
    }
    return render(request, 'geekshop/index.html', context=context)

def contacts(request):
    title = 'контакты'

    # if request.user.is_authenticated:
    #     basket = Basket.objects.filter(user=request.user)

    context = {
        'title': title,
        # 'basket': basket,
    }
    return render(request, 'geekshop/contact.html', context=context)
