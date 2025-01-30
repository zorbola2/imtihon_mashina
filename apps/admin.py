from django.contrib import admin
from django.apps import apps
from django.db.utils import IntegrityError
from .models import Brand, Cars

# Brand modelini admin panelga qo'shish
@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ('name',)

# Cars modelini admin panelga qo'shish
@admin.register(Cars)
class CarsAdmin(admin.ModelAdmin):
    list_display = ('nomi', 'brand_id', 'price', 'year', 'korobka')


