from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response

from base.products import products


@api_view(["GET"])
def get_routes(request):
    return Response("Hello")


@api_view(["GET"])
def get_products(request):
    return Response(products)


@api_view(["GET"])
def get_product_detail(request, pk):
    product = None

    for i in products:
        if i["_id"] == pk:
            product = i
            break

    return Response(product)
