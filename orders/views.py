from django.shortcuts import render,redirect
from django.views import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from .models import *
from shop.models import Cart


# Create your views here.
@method_decorator(login_required, name='dispatch')
class PlaceOrderView(View):
    def get(self,request):
        return render(request,'success.html')
    
    def post(self,request):
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        email = request.POST.get("email")
        address_1 = request.POST.get("address_1")
        address_2 = request.POST.get("address_2")
        pincode = request.POST.get("pincode")
        pay_option = request.POST.get("payment")

        order = Order.objects.create(
            user=request.user,
            full_name=name,phone=phone,
            email=email,address_1=address_1,address_2=address_2,
            pincode=pincode,pay_option=pay_option
        )
        total_amount = 0.0

        cart_items = Cart.objects.filter(user=request.user)
        for item in cart_items:
            OrderItem.objects.create(order=order,item_name=item.item.item_name,
                                     quantity=item.quantity,total_price=item.total_price)
        
            total_amount += item.total_price
        
        cart_items.delete()
        order.total_price = total_amount
        order.save()

        if pay_option == 'ONLINE':
            # create stripe payment link and redirect to the page
            return render(request,'pay_online.html',{'order':order})

        return render(request,'success.html',{'order':order})


@method_decorator(login_required, name='dispatch')
class OrderHistory(View):
    def get(self,request):
        orders = Order.objects.filter(user=request.user)
        return render(request,'history.html',{'orders':orders})