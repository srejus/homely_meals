from django.shortcuts import render,redirect
from django.views import View
from django.http import HttpResponse
from django.db.models import Sum
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from account.models import Account
from .models import *


# Create your views here.
class ShopView(View):
    def get(self,request,id=None):
        location = request.GET.get("location")
        if request.user.is_authenticated:
            acc = Account.objects.get(user=request.user)
            acc.place = location
            acc.save()
            
        shops = Shops.objects.filter(location=location).order_by('-is_open')
        if id:
            try:
                shop = Shops.objects.get(id=id)
            except Shops.DoesNotExist:
                return redirect("/shop")
            shop_imgs = ShopImages.objects.filter(shop=shop)
            products = Products.objects.filter(shop=shop)
            return render(request,'shop.html',{'shop':shop,'shop_imgs':shop_imgs,'products':products})
        
        return render(request,'shop_listing.html',{'shops':shops})
    

@method_decorator(login_required, name='dispatch')
class AddToCartView(View):
    def add_to_cart(self,id,user):
        try:
            item = Products.objects.get(id=id)
        except Products.DoesNotExist:
            return
        
        cart_obj = Cart.objects.filter(user=user,item=item)

        if cart_obj.exists():
            cart_obj = cart_obj.last()
            cart_obj.quantity += 1
            cart_obj.total_price += item.price
            cart_obj.save()
        else:
            cart_obj = Cart.objects.create(
                user=user,item=item,total_price=item.price
            )
        return
    
    def get(self,request,id):
        self.add_to_cart(id,request.user)
        return HttpResponse("Added to Cart")


@method_decorator(login_required, name='dispatch')
class RemoveFromCartView(View):
    def remove_from_cart(self,id,user):
        try:
            item = Products.objects.get(id=id)
        except Products.DoesNotExist:
            return
        
        cart_obj = Cart.objects.filter(user=user,item=item)

        if cart_obj.exists():
            cart_obj = cart_obj.last()
            if cart_obj.quantity == 1:
                cart_obj.delete()
                return
            
            cart_obj.quantity -= 1
            cart_obj.total_price -= item.price
            cart_obj.save()
       
        return
    
    def get(self,request,id):
        self.remove_from_cart(id,request.user)
        return HttpResponse("Removed from Cart")
    

@method_decorator(login_required, name='dispatch')
class CartView(View):
    def get(self,request):
        cart = Cart.objects.filter(user=request.user)
        total_price_sum = cart.aggregate(total_price_sum=Sum('total_price'))['total_price_sum']
        return render(request,'cart.html',{'products':cart,'total_amount':total_price_sum})
    

class ReviewView(View):
    def get(self,request,id):
        reviews = Review.objects.filter(shop__id=id)
        shop = Shops.objects.filter(id=id).last()
        return render(request,'reviews.html',{'reviews':reviews,'shop':shop})
    

@method_decorator(login_required, name='dispatch')
class RateStoreView(View):
    def calculate_rating(self,rating,shop):
        from decimal import Decimal,ROUND_HALF_DOWN

        reviews = Review.objects.filter(shop=shop)
        if reviews.exists():
            total_rating_sum = reviews.aggregate(rating_sum=Sum('rating'))
            total_rating = total_rating_sum.get('rating_sum') or Decimal('0')

            # Calculate the new total rating by adding the new rating to the existing total
            new_total_rating = total_rating + Decimal(rating)

            # Calculate the average rating
            total_reviews = reviews.count()
            avg_rating = (new_total_rating) / (total_reviews + 1)

            # Update the shop's rating
            shop.rating = avg_rating.quantize(Decimal('.01'))
        else:
            # If no existing reviews, set the rating directly
            shop.rating = Decimal(rating)

        shop.save()

        return
    
    def get(self,request,id):
        try:
            shop = Shops.objects.get(id=id)
        except Shops.DoesNotExist:
            return redirect(f"/shops/reviews/{id}")
        return render(request,'rate_shop.html',{'shop':shop})

    def post(self,request,id):
        rating = request.POST.get("rating")
        review = request.POST.get("review")
        try:
            shop = Shops.objects.get(id=id)
        except Shops.DoesNotExist:
            return redirect(f"/shop/reviews/{id}")

        Review.objects.create(
            shop=shop,rating=rating,review=review,user=request.user
        )
        self.calculate_rating(rating,shop)
        return redirect(f"/shop/reviews/{id}")
        