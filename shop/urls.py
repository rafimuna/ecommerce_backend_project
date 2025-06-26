from django.urls import path
from .views_cart import CartView
from .views_order import PlaceOrderView, UserOrderListView
from .views_payout import UserPayoutRequestView, AdminPayoutManageView
from .views import (
    ProductListView,
    ProductDetailView,
    ProductCreateView,
    ProductUpdateDeleteView,
    OrderListCreateView,
    PayoutRequestView,
    CategoryListView,
)

urlpatterns = [
    # 🛒 Cart
    path('cart/', CartView.as_view()),

    # 🛍️ Products
    path('products/', ProductListView.as_view()),                   # GET list
    path('products/create/', ProductCreateView.as_view()),          # POST create (admin)
    path('products/<int:id>/', ProductDetailView.as_view()),        # GET details
    path('products/<int:pk>/edit/', ProductUpdateDeleteView.as_view()),  # PUT/PATCH/DELETE

    # 📂 Categories
    path('categories/', CategoryListView.as_view()),                # GET all categories

    # 🧾 Order
    path('order/', PlaceOrderView.as_view()),                       # POST new order
    path('orders/', UserOrderListView.as_view()),                   # GET user orders

    # 💳 Payouts
    path('payout/request/', UserPayoutRequestView.as_view()),       # POST user request
    path('payouts/', PayoutRequestView.as_view()),                  # Admin/user list
]
