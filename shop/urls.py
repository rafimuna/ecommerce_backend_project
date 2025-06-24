from django.urls import path
from .views_cart import CartView
from .views_order import PlaceOrderView, UserOrderListView
from .views_payout import UserPayoutRequestView, AdminPayoutManageView
from .views import ProductListView,ProductDetailView, OrderListCreateView, PayoutRequestView

urlpatterns = [
    path('cart/', CartView.as_view()),
    path('order/', PlaceOrderView.as_view()),              # POST
    path('orders/', UserOrderListView.as_view()),          # GET
    path('products/', ProductListView.as_view()),
    path('payout/request/', UserPayoutRequestView.as_view()),  # POST
    path('products/<int:id>/', ProductDetailView.as_view(), name='product-detail'),
    path('payouts/', PayoutRequestView.as_view()),
]
