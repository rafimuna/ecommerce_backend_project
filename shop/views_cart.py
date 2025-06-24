# shop/views_cart.py

from .models import CartItem
from .serializers import CartItemSerializer
from rest_framework import generics, permissions, status
from rest_framework.response import Response

class CartView(generics.GenericAPIView):
    serializer_class = CartItemSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        items = CartItem.objects.filter(user=request.user)
        serializer = self.get_serializer(items, many=True)
        return Response(serializer.data)

    def post(self, request):
        data = request.data
        item, created = CartItem.objects.get_or_create(
            user=request.user,
            product_id=data['product_id'],
            defaults={'quantity': data.get('quantity', 1)}
        )
        if not created:
            item.quantity += data.get('quantity', 1)
            item.save()
        return Response({'success': True})

    def put(self, request):
        item = CartItem.objects.get(id=request.data['id'], user=request.user)
        item.quantity = request.data['quantity']
        item.save()
        return Response({'success': True})

    def delete(self, request):
        CartItem.objects.filter(id=request.data['id'], user=request.user).delete()
        return Response({'success': True})
