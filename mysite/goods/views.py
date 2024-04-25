from django.core.paginator import Paginator
from django.shortcuts import render
from django.template import context

from goods.models import Products

def catalog(request, page=1):
    goods = Products.objects.all()

    paginator = Paginator(goods, 3)
    current_page = paginator.page(page)

    context: dict[str, str] = {
        'title': 'Home - Каталог',
        'goods': current_page,
    }
    return render(request, 'goods/catalog.html', context)

def product(request, product_slug):
    product = Products.objects.get(slug=product_slug)

    context: dict[str, str] = {
        "product": product,
    }

    return render(request, 'goods/product.html', context=context)
