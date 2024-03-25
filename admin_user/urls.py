from django.urls import path
from .views import *

urlpatterns = [
    path('',AdminHomeView.as_view()),
    path('users',AdminUsersView.as_view()),
    path('orders',AdminOrdersView.as_view()),
    path('orders/<int:id>',AdminOrdersView.as_view()),
    path('shops',AdminShopsView.as_view()),
    path('shops/approve/<int:id>',AdminShopApproveView.as_view()),
    path('shops/reject/<int:id>',AdminShopRejectView.as_view()),
    path('reviews',AdminReviewsView.as_view()),
]