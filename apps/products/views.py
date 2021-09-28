from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import viewsets, generics
from .models import Product, Category
from .serializers import ProductSerializer, CategorySerializer


class CategoryView(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated, ]


class ProductView(viewsets.ModelViewSet):
    queryset = Product.objects.all().order_by('-id')
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated, ]

    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)

    @action(methods=['post', ], detail=True)
    def finished(self, request, pk=None):
        product = self.get_object()
        product.is_finished = not product.is_finished
        product.save()
        serializer = self.get_serializer(instance=product)
        return Response(serializer.data)
