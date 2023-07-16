from django.shortcuts import render

from catalog.models import Product


def home(request):
    product_list = Product.objects.all()
    context = {
        'object_list': product_list,
        'title': 'Pricing'
    }
    return render(request, 'catalog/home.html', context)


def sing_in(request):
    context = {
        'title': 'Sing-in'
    }
    return render(request, 'catalog/sing_in.html', context)