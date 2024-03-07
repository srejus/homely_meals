from django.shortcuts import render,redirect
from django.views import View

from account.models import Account
from shop.models import Shops


# Create your views here.
class IndexView(View):
    def get(self,request):
        if request.user.is_authenticated:
            if Shops.objects.filter(user=request.user).exists():
                return redirect("/shop/dashboard")
            acc = Account.objects.get(user=request.user)
            if acc.place:
                return redirect(f"/shop/?location={acc.place}")
        return render(request,'index.html')