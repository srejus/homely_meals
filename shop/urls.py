from django.urls import path
from .views import *

urlpatterns = [
    path('',ShopView.as_view()),
    path('<int:id>',ShopView.as_view()),
    path('add-to-cart/<int:id>',AddToCartView.as_view()),
    path('remove-from-cart/<int:id>',RemoveFromCartView.as_view()),
    path('cart',CartView.as_view()),
    path('reviews/<int:id>',ReviewView.as_view()),
    path('reviews/<int:id>/write',RateStoreView.as_view()),

    # shop dashboard session
    path('login',ShopLogin.as_view()),
    path('open/<int:id>',ShopOpenView.as_view()),
    path('close/<int:id>',ShopCloseView.as_view()),
    path('dashboard',ShopDashboardView.as_view()),
    path('manage-stock',ShopStockView.as_view()),
    path('orders',ShopOrderView.as_view()),
    path('orders/<int:id>',ShopOrderView.as_view()),
    path('manage-stock/<int:id>',ShopStockView.as_view()),
]