from fl.models import Product, Image

def fetch_categories():
    unique_categories = Product.objects.values_list('category', flat=True).distinct()
    return unique_categories

def fetch_products(category):
    products = Product.objects.filter(category=category).values('name', 'sku','main_image_url','price')
    return products

def fetch_product_detail(sku):
    product = Product.objects.filter(sku=sku).values().first()
    images = Image.objects.filter(sku=sku).values_list('image_url', flat=True)
    stock_val = None
    if product and product.get('stock'):
        stock_str = product.get('stock')
        stock = int(stock_str)
        
        if stock == 0:
            stock_val = 'Agotado'
        elif stock > 0  and stock <= 10:
            stock_val = 'Pocas Unidades'
        elif stock > 10:
            stock_val = 'Disponible'
    return product,images,stock_val

def search_product(search_variable):
    if not search_variable:
        return None, None
    product = Product.objects.filter(sku=search_variable).values().first()
    if not product:
        product = Product.objects.filter(name__icontains=search_variable).values().first()
    if product:
        sku = product.get('sku')
    else:
        return None, None
    images = Image.objects.filter(sku=sku).values_list('image_url', flat=True)
    stock_val = None
    if product and product.get('stock'):
        stock_str = product.get('stock')
        stock = int(stock_str)
        
        if stock == 0:
            stock_val = 'Agotado'
        elif stock > 0  and stock <= 10:
            stock_val = 'Pocas Unidades'
        elif stock > 10:
            stock_val = 'Disponible'

    return product,images,stock_val