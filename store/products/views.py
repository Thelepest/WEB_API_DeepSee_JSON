from products.models import Product
from django.http import JsonResponse
import json


def product_list(request):
    products = Product.objects.all()
    data = {"products" : list(products.values())}
    response = JsonResponse(data)
    return response

def add_product(request):
    if request.method == 'POST':
        json_data = json.loads(request.body)
        new_name = json_data['name']
        new_amount = json_data['amount_in_stock']

        try:
            product = Product.objects.get(name=new_name)
            product.amount_in_stock += new_amount
        except Product.DoesNotExist :
            product = Product()
            product.name = new_name
            product.amount_in_stock = new_amount

        product.save()

        data = {"product saved " : [product.name, product.amount_in_stock]}
        response = JsonResponse(data)
        return response

def order(request):
    if request.method == 'POST':
        json_data = json.loads(request.body)
        new_name = json_data['name']
        new_amount = json_data['amount_in_stock']
        try:
            product = Product.objects.get(name=new_name)
            product.amount_in_stock -= new_amount
            data = {"order saved " : [new_name, new_amount]}
            product.save()
        except Product.DoesNotExist :
            data = {"Error. Product doesn't exist or not available" : [new_name, new_amount]}

        response = JsonResponse(data)
        return response
