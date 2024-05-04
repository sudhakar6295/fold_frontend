from django.shortcuts import render
from fl.extraction.data_extraction import fetch_categories,fetch_products,fetch_product_detail

# Create your views here.
def index(request):
    categorys = fetch_categories()
    return render(request, 'index.html',{'categorys':categorys})

def category_view(request, category):
    products = fetch_products(category)
    return render(request, 'category.html',{'products':products})


def product_detail(request, category,sku):
    product,images = fetch_product_detail(sku)
    return render(request, 'product_detail.html',{'product':product,'images':images})
