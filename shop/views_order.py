# shop/views_order.py
# shop/views_order.py

from rest_framework import permissions, generics
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Order, OrderItem, CartItem
from .serializers import OrderSerializer

class PlaceOrderView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        cart_items = CartItem.objects.filter(user=request.user)
        if not cart_items.exists():
            return Response({'error': 'Cart is empty'}, status=400)

        total = sum(item.product.price * item.quantity for item in cart_items)
        order = Order.objects.create(user=request.user, total=total)

        for item in cart_items:
            OrderItem.objects.create(order=order, product=item.product, quantity=item.quantity)

        cart_items.delete()
        return Response({'success': True, 'order_id': order.id})

class UserOrderListView(generics.ListAPIView):
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user).prefetch_related('items__product')



