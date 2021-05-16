from django.shortcuts import render

from product.models import Product

# Create your views here.
def home(request):
    newest_products = Product.objects.all()[0:8]
    
    context = {
        'newest_products' : newest_products,
    }
    return render(request, 'core/home.html', context)