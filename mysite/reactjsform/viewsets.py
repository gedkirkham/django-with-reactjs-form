from reactjsform.models import Product
from rest_framework import viewsets
from reactjsform.serialiser import ProductSerialiser

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerialiser