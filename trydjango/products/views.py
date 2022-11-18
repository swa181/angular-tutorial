from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from .models import Product

from .forms import ProductForm


def product_create_view(request, *args, **kwargs):
    form = ProductForm()
    if request.method == "POST":
        form = ProductForm(request.POST)
    if form.is_valid():
        Product.objects.create(**form.cleaned_data)
        print(form.cleaned_data)

    context = {'form': form}
    return render(request, "products/product_create.html", context)

# def product_create_view(request, *args, **kwargs):
#     form = RawProductForm()
#     if request.method == "POST":
#         form = RawProductForm(request.POST)
#     if form.is_valid():
#         Product.objects.create(**form.cleaned_data)
#         print(form.cleaned_data)

#     context = {'form': form}
#     return render(request, "products/product_create.html", context)


def product_detail_view(request, *args, **kwargs):
    obj = Product.objects.get(id=1)
    # context = {
    #     'title': obj.title,
    #     'description': obj.description
    # }
    context = {'obj': obj}
    return render(request, "products/product_detail.html", context)
