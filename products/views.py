from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Product
from .serializers import ProductSerializer, PurchaseSerializer

class ProductListCreateView(generics.ListCreateAPIView):
    queryset = Product.objects.filter(is_sold=False)
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(seller=self.request.user)

class ProductDetailView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]

class PurchaseProductView(generics.UpdateAPIView):
    queryset = Product.objects.filter(is_sold=False)
    serializer_class = PurchaseSerializer
    permission_classes = [IsAuthenticated]

    def update(self, request, *args, **kwargs):
        product = self.get_object()
        if product.seller == request.user:
            return Response({"detail": "Seller cannot buy their own product."}, status=status.HTTP_400_BAD_REQUEST)
        return super().update(request, *args, **kwargs)
