from rest_framework import viewsets, status
from rest_framework.exceptions import NotAcceptable
from rest_framework.response import Response
from rest_framework.views import APIView

from djshop.apps.catalog.models import Category, Option, ProductClass, Product, ProductRecommendation
from djshop.apps.catalog.serializers.admin import CreateCategoryNodeSerializer, CategoryTreeSerializer, \
    CategoryNodeSerializer, CategoryModificationSerializer, ProductSerializer, ProductClassSerializer


class CategoryViewSet(viewsets.ModelViewSet):

    def get_queryset(self):
        if self.action == 'list':
            return Category.objects.filter(depth=1)
        else:
            return Category.objects.all()

    def  get_serializer_class(self):
        match self.action:
            case 'list':
                return CategoryTreeSerializer
            case 'create':
                return CreateCategoryNodeSerializer
            case 'retrieve':
                return CategoryNodeSerializer
            case 'update':
                return CategoryModificationSerializer
            case 'partial_update':
                return CategoryModificationSerializer
            case 'destroy':
                return CategoryModificationSerializer

            case _:
                raise NotAcceptable()



class ProductViewSet(viewsets.ModelViewSet):

    def get_queryset(self):
        return Product.objects.all()

    def get_serializer_class(self):
        return ProductSerializer



class ProductClassViewSet(viewsets.ModelViewSet):

    def get_queryset(self):
        return ProductClass.objects.all()

    def get_serializer_class(self):
        return ProductClassSerializer


