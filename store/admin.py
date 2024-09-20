from django.contrib import admin
from .models import Category, Product

# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug'] # displays the category data entries as a list where each row in list is
    prepopulated_fields = {'slug': ('name',)} # since the slug is an URL friendly formatted version of the category name, it is prepopulated whenever the name of the category is typed in

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'slug', 'price', 'in_stock', 'created', 'updated']
    list_filter = ['in_stock', 'is_active'] # creates filters
    list_editable = ['price', 'in_stock'] # these fields can be edited in bulk
    prepopulated_fields = {'slug': ('title',)}