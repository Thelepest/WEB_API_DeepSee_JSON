from django.urls import path

from products.views import product_list, add_product, order

urlpatterns = [
    path('products/',product_list,name="product-list"),
    path('add/',add_product, name="add-product"),
    path('order/',order,name="add-order")
]