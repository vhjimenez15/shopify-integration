from rest_framework.viewsets import GenericViewSet
from rest_framework.views import Response
from django.conf import settings
import requests


class ProductViews(GenericViewSet):

    def list(self, request, *args, **kwargs):
        base_url = settings.SHOPIFY_BASE_URL
        response = requests.get(
            f"{base_url}/products.json",
            headers={
                "Content-Type": "application/json",
                "X-Shopify-Access-Token": settings.SHOPIFY_ADMIN_KEY
            }
        )
        return Response({"message": "OK", "data": response.json()})


class CustomerViews(GenericViewSet):

    def list(self, request, *args, **kwargs):
        base_url = settings.SHOPIFY_BASE_URL
        response = requests.get(
            f"{base_url}/customers.json",
            headers={
                "Content-Type": "application/json",
                "X-Shopify-Access-Token": settings.SHOPIFY_ADMIN_KEY
            }
        )
        return Response({"message": "OK", "data": response.json()})


class OrderViews(GenericViewSet):

    def list(self, request, *args, **kwargs):
        params = request.query_params
        base_url = settings.SHOPIFY_BASE_URL
        params_dict = {}
        if name := params.get("name"):
            params_dict.update({"name": name})
        if financial_status := params.get("financial_status"):
            params_dict.update({"financial_status": financial_status})

        response = requests.get(
            f"{base_url}/orders.json",
            headers={
                "Content-Type": "application/json",
                "X-Shopify-Access-Token": settings.SHOPIFY_ADMIN_KEY
            },
            params=params_dict
        )
        return Response({"message": "OK", "data": response.json()})


class InventoryLocationViews(GenericViewSet):

    def list(self, request, *args, **kwargs):
        base_url = settings.SHOPIFY_BASE_URL
        response = requests.get(
            f"{base_url}/locations.json",
            headers={
                "Content-Type": "application/json",
                "X-Shopify-Access-Token": settings.SHOPIFY_ADMIN_KEY
            }
        )
        return Response({"message": "OK", "data": response.json()})
