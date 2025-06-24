# shop/views_payout.py

from rest_framework import generics, permissions
from rest_framework.response import Response
from .models import PayoutRequest
from .serializers import PayoutRequestSerializer


class UserPayoutRequestView(generics.CreateAPIView):
    serializer_class = PayoutRequestSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class AdminPayoutManageView(generics.ListAPIView):
    serializer_class = PayoutRequestSerializer
    permission_classes = [permissions.IsAdminUser]

    def get_queryset(self):
        return PayoutRequest.objects.all().select_related('user')
