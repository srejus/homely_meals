from django.shortcuts import render,redirect
from django.views import View

from .models import *
from account.models import *
from home.models import *
from orders.models import *
from shop.models import *

from django.db.models import Q

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


# Create your views here.
@method_decorator(login_required,name='dispatch')
class AdminHomeView(View):
    def get(self,request):
        if not request.user.is_superuser:
            msg = "You don't have access to this page"
            return redirect(f"/?msg={msg}")
        return render(request,'admin_dashboard.html')



@method_decorator(login_required,name='dispatch')
class AdminUsersView(View):
    def get(self,request):
        if not request.user.is_superuser:
            msg = "You don't have access to this page"
            return redirect(f"/?msg={msg}")
        
        users = Account.objects.all().order_by('-id')
        term = request.GET.get("term")
        if term:
            users = Account.objects.filter(Q(user__first_name__icontains=term) |
                                            Q(place__icontains=term)).order_by('-id')
        return render(request,'admin_users.html',{'users':users})
    


@method_decorator(login_required,name='dispatch')
class AdminOrdersView(View):
    def get(self,request,id=None):
        if not request.user.is_superuser:
            msg = "You don't have access to this page"
            return redirect(f"/?msg={msg}")
        
        if id:
            order = Order.objects.get(id=id)
            order_items = OrderItem.objects.filter(order=order)
            return render(request,'admin_order_view.html',{'items':order_items})

        orders = Order.objects.all().order_by('-id')
        return render(request,'admin_orders.html',{'orders':orders})
    


@method_decorator(login_required,name='dispatch')
class AdminShopsView(View):
    def get(self,request):
        if not request.user.is_superuser:
            msg = "You don't have access to this page"
            return redirect(f"/?msg={msg}")
        
        shops = Shops.objects.all().order_by('-id')
        return render(request,'admin_shops.html',{'shops':shops})
    


@method_decorator(login_required,name='dispatch')
class AdminReviewsView(View):
    def get(self,request):
        if not request.user.is_superuser:
            msg = "You don't have access to this page"
            return redirect(f"/?msg={msg}")
        
        reviews = Review.objects.all().order_by('-id')
        term = request.GET.get("term")
        if term:
            reviews = Review.objects.filter(
                Q(shop__shop_name__icontains=term) |
                 Q(user__first_name__icontains=term) | 
                  Q(review__icontains=term)).order_by('-id')
        return render(request,'admin_reviews.html',{'reviews':reviews})
    

@method_decorator(login_required,name='dispatch')
class AdminShopApproveView(View):
    def get(self,request,id=None):
        if not request.user.is_superuser:
            msg = "You don't have access to this page"
            return redirect(f"/?msg={msg}")
        
        Shops.objects.filter(id=id).update(approved=True)
        return redirect("/admin-user/shops")
        
    
@method_decorator(login_required,name='dispatch')
class AdminShopRejectView(View):
    def get(self,request,id=None):
        if not request.user.is_superuser:
            msg = "You don't have access to this page"
            return redirect(f"/?msg={msg}")
        
        Shops.objects.filter(id=id).update(approved=False)
        return redirect("/admin-user/shops")
        
        