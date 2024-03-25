from django.urls import path
from .views import *


urlpatterns = [
    path('',ProfileView.as_view()),
    path('login/',LoginView.as_view()),
    path('signup',SignupView.as_view()),
    path('logout',LogoutView.as_view()),

    path('shop-reg',ShopRegView.as_view()),
]