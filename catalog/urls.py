from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import ProductListView, sing_in

app_name = CatalogConfig.name

urlpatterns = [
    path('', ProductListView.as_view(), name='home'),
    path('contact/', sing_in, name='sing_in')
]
