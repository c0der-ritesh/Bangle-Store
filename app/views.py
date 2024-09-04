from django.shortcuts import render, HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from app.models import UserDetail
from app.models import ProductDetail
from app.models import CartDetail
from app.models import OrderDetail
from django.utils.encoding import smart_str
from django.template.loader import render_to_string
from datetime import datetime, date,timedelta
#@login_required(login_url='login')
def home(request):
 Productdata = ProductDetail.objects.all()
 productreverse = reversed(Productdata)
 data={
  'Productdata':Productdata,
  'productreverse':productreverse
 }
 return render(request, 'app/home.html',data)

@login_required(login_url='login')
def product_detail(request):
 value = request.GET.get('value')
 value2 = request.GET.get('value2')
 value3 = request.GET.get('value3')
 #value = ProductDetail.objects.all() 
 return render(request, 'app/productdetail.html',{'value':value,'value2':value2,'value3':value3})

@login_required(login_url='login')
def add_to_cart(request):
  #if request.method=="POST":
   pname = request.GET.get('pname')
   pdesc = request.GET.get('pdesc')
   pr = request.GET.get('price')
   price = float(pr.replace(',', ''))
   shipprice = float(70.00)
   if request.user.is_authenticated:
    name = request.user
   en = CartDetail(productname=pname,productdesc=pdesc,price = price,shipprice=shipprice,Name=name)
   en.save()
   #Cartdetail = CartDetail.objects.all()
   if request.user.is_authenticated:
    N = request.user
   Cartdetail = CartDetail.objects.filter(Name=N)
   total_price = sum(n.price for n in Cartdetail) + 70.00
   data={
  'Cartdetail':Cartdetail,
  'total_price':total_price
   }
   return render(request,'app/addtocart.html',data)
#return render(request, 'app/addtocart.html',{'pname':pname,'pdesc':pdesc,'price':float(price),'shipprice':float(shipprice)})

@login_required(login_url='login')
def final_add_to_cart(request):
 #Cartdetail = CartDetail.objects.all()
 total_price = 0.0
 if request.user.is_authenticated:
   N = request.user
 Cartdetail = CartDetail.objects.filter(Name=N)
 count = Cartdetail.count()
 for n in Cartdetail:
  total_price = sum(n.price for n in Cartdetail) + 70.00
 data = {
  'Cartdetail':Cartdetail,
  'total_price':total_price,
  'count':count
 }
 return render(request,'app/final-add-cart.html',data)



@login_required(login_url='login')
def buy_now(request):
 return render(request, 'app/buynow.html')



@login_required(login_url='login')
def profile(request):
 if request.method=="POST":
  name = request.POST.get('name')
  Address = request.POST.get('Address')
  Address1 = request.POST.get('Address1')
  City = request.POST.get('City')
  State = request.POST.get('State')
  Zip = request.POST.get('Zip')

  en = UserDetail(Name=name,Address=Address,Adress1=Address1,City=City,State=State,Zip=Zip)
  en.save()
  return redirect('address')
  #print(name)
  
 return render(request, 'app/profile.html')




@login_required(login_url='login')
def address(request):
 Userdata = UserDetail.objects.all()
 data={
  'Userdata':Userdata
 }
 return render(request, 'app/address.html',data)

@login_required(login_url='login')
def payment(request):
 return render(request,'app/payment.html')



@login_required(login_url='login')
def orders(request):
 Orderdata = OrderDetail.objects.all()
 data={
   'Orderdata':Orderdata
 }
 return render(request, 'app/orders.html',data)

@login_required(login_url='login')
def change_password(request):
 return render(request, 'app/changepassword.html')

def Gold(request):
 return render(request, 'app/Gold.html')

def get_user(email):
    try:
        return User.objects.get(email=email.lower())
    except User.DoesNotExist:
        return None

#@login_required
def userlogin(request):
 if request.method=='POST':
  email = request.POST.get('email')
  password = request.POST.get('pass')
  username = get_user(email)
  user = authenticate(request,username=username,password=password)
  if user is not None:
   login(request,user)
   return redirect('home')
  else:
   error = "User Not Exist"
   return render(request, 'app/login.html', {'error': error})

 return render(request, 'app/login.html')

def customerregistration(request):
 if request.method=='POST':
  uname = request.POST.get('name')
  email = request.POST.get('email')
  password = request.POST.get('password')
  confirmpassword = request.POST.get('password1')
  if password!=confirmpassword:
    error = "Password and Confirm Password not matched"
    return render(request, 'app/customerregistration.html', {'error': error})
  else:
   my_user = User.objects.create_user(uname,email,confirmpassword)
   my_user.save()
   return redirect('login')
 return render(request, 'app/customerregistration.html')

def logoutpage(request):
 logout(request)
 return redirect('login')
 
@login_required(login_url='login')
def checkout(request):
 
 if request.user.is_authenticated:
   N = request.user
 Cartdetail = CartDetail.objects.filter(Name=N)
 count = Cartdetail.count()
 Userdata = UserDetail.objects.filter(Name=N)
 for n in Cartdetail:
  total_price = sum(n.price for n in Cartdetail) + 70.00
 current_date = date.today()
 new_date = current_date + timedelta(days=3)
 new_date1 = current_date + timedelta(days=5)
 #print(current_date)
 data = {
  'Cartdetail':Cartdetail,
  'total_price':total_price,
  'count':count,
  'Userdata':Userdata,
  'current_date':current_date,
  'new_date':new_date,
  'new_date1':new_date1
 }
 for n in Cartdetail:
  pname = n.productname
  consumername = n.Name
 if request.user.is_authenticated:
   X = request.user
 Udetail = UserDetail.objects.filter(Name=X)
 for n in Udetail:
  ad = n.Address
  city = n.City
  state = n.State
  pin = n.Zip
 en = OrderDetail(Name=X,Netprice=total_price,Address=ad,State=state,City=city,Zip=pin,Date=new_date1)
 en.save()
 dawnload()

 return render(request, 'app/checkout.html',data)

def gen_file():
 data = OrderDetail.objects.all()
 file_content = ''
 for item in data:
        # Adjust formatting as needed
      file_content += f"{item.Name}, {item.Address}, {item.City},{item.State},{item.Zip},{item.Netprice}\n"

 return file_content

def dawnload():
   file_content = gen_file()

    # Create a response object with appropriate headers
   response = HttpResponse(content_type='text/plain')
   response['Content-Disposition'] = 'attachment; filename="data.txt"'
    
    # Write the file content to the response
   response.write(smart_str(file_content))

   return response




