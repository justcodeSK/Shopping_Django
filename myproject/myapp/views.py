from django.shortcuts import render,redirect
from myapp.models import Users,Cart,Products
from django.contrib.auth import authenticate,login,logout
from django.db.models import Sum
import os


# Create your views here.
def home(request):
    return render(request,'home.html')

def reg(request):
    if request.method=='POST':
        nm=request.POST['name']
        em=request.POST['email']
        ad=request.POST['address']
        ge=request.POST['gender']
        ag=request.POST['age']
        pwd=request.POST['pwd']
        cpwd=request.POST['cpwd']
        x=Users.objects.create(Name=nm,Email=em,Address=ad,Gender=ge,Age=ag,Password=pwd,Cpassword=cpwd)
        x.save()
        return redirect(reg)
    else:
        return render(request,'reg.html')   


def admin(request):
     if request.method == 'POST':
        file=request.FILES['image']
        fname=file.name.split('/')[-1]
        filepath="\static\images\\"+fname
        im=filepath
        nm=request.POST['name']
        pr=request.POST['price']
        dis=request.POST['description']
        x=Products.objects.create(Image=im,Name=nm,Price=pr,Description=dis)
        x.save()
        return redirect(admin)
     else:
        return render(request,'admin.html')
def productadm(request):
      x=Products.objects.all()
      return render(request,'productadm.html',{'da':x})
def update(request,uid):
    if request.method == 'GET':
        x=Products.objects.get(id=uid)
        return render(request,'update.html',{'da':x})
    elif request.method == 'POST':
        im=request.POST['image']
        nm=request.POST['name']
        pr=request.POST['price']
        dis=request.POST['description']
        x=Products.objects.filter(id=uid).update(Image=im,Name=nm,Price=pr,Description=dis)
        return redirect(productadm)
def delete(request,uid):
    x=Products.objects.get(id=uid)
    x.delete()
    return redirect(productadm)


def login(request):
    if request.method=='POST':
        USERNAME=request.POST['email']
        PASSWORD=request.POST['pwd']
        users=authenticate(username=USERNAME,password=PASSWORD)
        if users is not None and users.is_superuser == 1:
            return redirect(admin)
        if Users.objects.filter(Email=USERNAME,Password=PASSWORD).exists():
            usr=Users.objects.filter(Email=USERNAME,Password=PASSWORD)
            for i in usr:
                request.session['user_id']=i.id
                return redirect(user)
    else:
        return render(request,'login.html')
def logout(request):
    return redirect(home)
    

def user(request):
        x=Products.objects.all()
        return render(request,'user.html',{'da':x}) 
def addcart(request, uid):
    product = Products.objects.get(id=uid)
    im=product.Image
    nm=product.Name
    pr=product.Price
    check=Cart.objects.filter(id=uid).first()
    if check:
        check.Quantity+=1
        check.save()
    else:
        x=Cart.objects.create(Image=im, Name=nm, Price=pr, Quantity=1)
        x.save()
    totalqty(request)
    return redirect('user')
def cart(request):
    x=Cart.objects.all()
    return render(request, 'cart.html', {'da': x, 'total': request.session.get('total', 0)})
def cartdel(request,uid):
    x=Cart.objects.get(id=uid)
    x.delete()
    totalqty(request)
    return redirect(cart)
def totalqty(request):
    total = Cart.objects.aggregate(sum_quantity=Sum('Quantity'))['sum_quantity']
    if total is None:
        total = 0
    request.session['total'] = total





        