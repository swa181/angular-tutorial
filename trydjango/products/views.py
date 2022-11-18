from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from .models import Product

from .forms import ProductForm


def product_list_view(req):
    queryset = Product.objects.all()
    context = {'object_list': queryset}
    return render(req, "products/product_list.html", context)


def product_delete_view(request, id):
    obj = get_object_or_404(Product, id=id)

    if request.method == 'POST':
        obj.delete()
        return redirect('../')

    context = {
        "object": obj
    }
    return render(request, "products/product_delete.html", context)


def product_detail_view(request, id):
    obj = get_object_or_404(Product, id=id)
    context = {
        "object": obj
    }
    return render(request, "products/product_detail.html", context)


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


# def product_detail_view(request, *args, **kwargs):
#     obj = Product.objects.get(id=1)
#     # context = {
#     #     'title': obj.title,
#     #     'description': obj.description
#     # }
#     context = {'obj': obj}
#     return render(request, "products/product_detail.html", context)
