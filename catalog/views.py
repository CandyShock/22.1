from django.shortcuts import render
from django.views.generic import ListView
from catalog.models import Product


class ProductListView(ListView):
    model = Product
    template_name = 'catalog/home.html'


def sing_in(request):
    context = {
        'title': 'Sing-in'
    }
    return render(request, 'catalog/sing_in.html', context)
