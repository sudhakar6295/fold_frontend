from django.shortcuts import render
from fl.extraction.data_extraction import fetch_categories,fetch_products,fetch_product_detail,search_product
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
# Create your views here.
def index(request):
    categorys = fetch_categories()
    return render(request, 'index.html',{'categorys':categorys})

def category_view(request, category,page=1):
    products = fetch_products(category)
    page = request.GET.get('page', 1)
    paginator = Paginator(products, 20)
    try:
        items = paginator.page(page)
    except PageNotAnInteger:
        items = paginator.page(1)
    except EmptyPage:
        items = paginator.page(paginator.num_pages)
    return render(request, 'category.html',{'products':items,'page':items})


def product_detail(request, category,sku):
    
    product,images = fetch_product_detail(sku)
    return render(request, 'product_detail.html',{'product':product,'images':images})

def search(request):
    if request.method == 'GET' and 'query' in request.GET:
        query = request.GET['query']
        product, images = search_product(query)
        if product :
            return render(request, 'product_detail.html', {'product': product, 'images': images})
    
    categorys = fetch_categories()
    return render(request, 'index.html', {'categorys': categorys})

