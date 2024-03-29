import random

from .models import Category, Product

from django.db.models import Q

from django.shortcuts import get_object_or_404, render

# Create your views here.
def product(request, category_slug, product_slug):
    product = get_object_or_404(Product, category__slug=category_slug,slug=product_slug)

    similar_products = list(product.category.products.exclude(id=product.id))

    if len(similar_products) >= 4:
        similar_products = random.sample(similar_products, 4)
    
    context = {
        'product' : product,
        'similar_products' : similar_products,
    }
    return render(request, 'product/product.html', context)

def category(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)

    context = {
        'category' : category,
    }

    return render(request, 'product/category.html', context)

# Search...
def search(request):
    query = request.GET.get('query', '')
    categorySelected = request.GET.get('categorySelected','')
    # print(categorySelected)
    if categorySelected != 'All':
        products = Product.objects.filter(category__title=categorySelected).filter(Q(title__icontains=query) | Q(description__icontains=query))
    else:
        products = Product.objects.filter(Q(title__icontains=query) | Q(description__icontains=query))
    context = {
        'query' : query,
        'products' : products,
    }
    return render(request, 'product/search.html', context)