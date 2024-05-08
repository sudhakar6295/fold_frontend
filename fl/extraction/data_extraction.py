from fl.models import Product, Image

def fetch_categories():
    unique_categories = Product.objects.values_list('category', flat=True).distinct()
    return unique_categories

def fetch_products(category):
    products = Product.objects.filter(category=category).values('name', 'sku','main_image_url')
    return products

def fetch_product_detail(sku):
    product = Product.objects.filter(sku=sku).values().first()
    images = Image.objects.filter(sku=sku).values_list('image_url', flat=True)
    return product,images

def search_product(sku):
    product = Product.objects.filter(sku='920309-01').values().first()
    images = Image.objects.filter(sku=sku).values_list('image_url', flat=True)
    return product,images