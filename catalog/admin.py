from django.contrib import admin

from catalog.models import Product, Category


# admin.site.register(Product)
# admin.site.register(Category)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'nomination', 'price', 'category')
    list_filter = ('category',)
    search_fields = ('nomination', 'description')


@admin.register(Category)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'nomination')
    list_filter = ('nomination',)
    search_fields = ('nomination', 'description')
