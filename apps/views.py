from django.shortcuts import render
from .models import Cars, Brand

# Create your views here.
def home_page(request):
    cars = Cars.objects.all()
    brands = Brand.objects.all()
    top_three_cars = Cars.objects.all()[:3]
   
    context = {
        'cars': cars,
        'brands': brands,
        'top_three_cars': top_three_cars,
    }
    return render(request, 'index.html', context)
