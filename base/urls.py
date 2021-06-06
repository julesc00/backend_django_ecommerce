from django.urls import path

from base.views import get_routes, get_products, get_product_detail

app_name = "base"

urlpatterns = [
    path("", get_routes, name="routes"),
    path("products/", get_products, name="products"),
    path("products/<str:pk>/", get_product_detail, name="product"),
]
