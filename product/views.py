from django.shortcuts import render
from django.http import HttpResponse

from .models import Product


def index(request):
    return HttpResponse("Hello, world. You're at the products index.")


def index_html_test(request):
    content_to_be_served = {
        "text_to_be_rendered": "This is the products page where you will find tons of Products being sold on Samana",
        "list_example": ['Product1', 'Product2', 420]
    }
    return render(request, 'product_index.html', content_to_be_served)


def product_list_view(request):
    obj_list = Product.objects.all()
    print(obj_list)
    return render(request, 'all_products.html', {'obj_list': obj_list})


def product_detail_view(request, pk):
    product = Product.objects.get(id=pk)
    return render(request, 'product_detail.html', {'obj': product})
