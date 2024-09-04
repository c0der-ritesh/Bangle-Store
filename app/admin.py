from django.contrib import admin
from app.models import UserDetail
from app.models import ProductDetail
from app.models import CartDetail
from app.models import OrderDetail

class UserAdmin(admin.ModelAdmin):
    list_display=('Name','Address','Adress1','City','State','Zip')

class ProductAdmin(admin.ModelAdmin):
    list_display=('pname','pdesc','price')

class CartAdmin(admin.ModelAdmin):
    list_display=('productname','productdesc','price','shipprice','Name')
class OrderAdmin(admin.ModelAdmin):
    list_display=('Name','Netprice','Address','State','City','Zip','Date')

admin.site.register(UserDetail,UserAdmin)
admin.site.register(ProductDetail,ProductAdmin)
admin.site.register(CartDetail,CartAdmin)
admin.site.register(OrderDetail,OrderAdmin)


# Register your models here.
