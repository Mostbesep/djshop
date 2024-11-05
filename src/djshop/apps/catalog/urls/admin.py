from django.urls import path
from rest_framework.routers import SimpleRouter


from djshop.apps.catalog.views.admin import CategoryViewSet, ProductViewSet, ProductClassViewSet

router = SimpleRouter()
router.register('categories',CategoryViewSet , basename='Category')
router.register('productClasses',ProductClassViewSet , basename='ProductClass')
router.register('products',ProductViewSet , basename='Products')


urlpatterns = [] + router.urls