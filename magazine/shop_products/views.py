from django.shortcuts import render
from django.http import HttpResponse
from .models import Product


def home(request):
    return render(request, 'shop_products/index.html', {})


def prod_list(request, *args, **kwargs):
    products = Product.objects.all()
    return render(request, 'shop_products/page_list.html', context={"products": products})


# def fir_page(request, *args, **kwargs):
#     return render(request, 'shop_products/page_list.html', {})
#
#
# def page_two(request,*args, **kwargs):
#     return render(request, 'shop_products/page_list.html')


def prod_detail(request, slug):
    product = Product.objects.get(slug__iexact=slug)
    return render(request, 'shop_products/page_detail.html', context={'product': product})
