from django.urls import path
from . import views  # Import views from the same directory

urlpatterns = [
    path('', views.index, name='index'),  # Define a URL pattern for the homepage
    path('search/', views.search, name='search'),
    path('<str:category>/', views.category_view, name='category_view'),
    path('<str:category>/<str:sku>/', views.product_detail, name='product_detail'),
    
]
