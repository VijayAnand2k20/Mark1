from product.models import Category

def menu_categories(reuqest):
    categories = Category.objects.all()

    return {'menu_categories' : categories}