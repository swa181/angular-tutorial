from django.urls import path
from .views import (
    product_create_view,
    product_detail_view,
    product_delete_view,
    product_list_view
)

app_name = 'products'

urlpatterns = [
    path('create/', product_create_view),
    path('<int:id>/', product_detail_view, name='product-detail'),
    path('<int:id>/delete/', product_delete_view),
    path('', product_list_view),
]
