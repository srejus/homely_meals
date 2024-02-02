from django.urls import path
from .views import *


urlpatterns = [
    path('place-order',PlaceOrderView.as_view()),
    path('history',OrderHistory.as_view()),
]