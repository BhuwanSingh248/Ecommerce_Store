from django.contrib import admin

from .models import Category, Product


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug':('name',)}  #  by defaut slug name will be same as catgory name till we are not changing that 

@admin.register(Product)
class ProducAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'slug', 'price', 'in_stock', 'create', 'update']
    list_filter = ['in_stock', 'is_active']
    list_editable=['price', 'in_stock']
    repopulated_fields = {'slug':('title',)}