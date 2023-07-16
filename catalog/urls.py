from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import home, sing_in

app_name = CatalogConfig.name

urlpatterns = [
    path('', home, name='home'),
    path('contact/', sing_in, name='sing_in')
]
