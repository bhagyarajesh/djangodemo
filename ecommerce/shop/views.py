
from shop.models import Category,Product

from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate,logout
from django.http import HttpResponse
# Create your views here.
def categories(request):
    c=Category.objects.all()
    context={'cat':c}
    return render(request,'categories.html',context)

def products(request,i):
    c=Category.objects.get(id=i)
    p=Product.objects.filter(category=c)
    context={'cat':c,'pro':p}
    return render(request,'product.html',context)

def productdetail(request,i):
    p = Product.objects.get(id=i)
    context = {'pro': p}
    return render(request, 'detail.html', context)

def register(request):
    if(request.method=="POST"):
        u = request.POST['u']
        p = request.POST['p']
        cp = request.POST['cp']
        e = request.POST['e']
        f = request.POST['f']
        l = request.POST['l']

        if(p==cp):
            v=User.objects.create_user(username=u,password=p,email=e,first_name=f,last_name=l)
            v.save()
        else:
            return HttpResponse("Passwords should be same")

        return redirect('shop:categories')

    return render(request,'register.html')

#add books
def user_login(request):
    if(request.method=="POST"):
        u = request.POST['u']
        p = request.POST['p']

        user=authenticate(username=u,password=p) #checks whether the details entered by the user is correct or not

        if user: #if user already exists
            login(request,user)
            return redirect('shop:categories')
        else: #if user does not exists
            return HttpResponse("invalid credentials")
    return render(request,'login.html')

def user_logout(request):
    logout(request)
    return redirect("shop:login")

def addcategories(request):
    if (request.method == "POST"):
        n = request.POST['n']
        i = request.FILES['i']
        d = request.POST['d']
        a = Category.objects.create(name=n, image=i, desc=d)  # creates a new record
        a.save()  # saves the record inside the table Book
        return redirect('shop:categories')

    return render(request, 'addcategories.html')

def addproducts(request):
    if (request.method == "POST"):
        n = request.POST['n']
        i = request.FILES['i']
        d = request.POST['d']
        s = request.POST['s']
        p = request.POST['p']
        c=request.POST['c']  #category name
        cat=Category.objects.get(name=c)  #Retrieve a category record matching with that name
        a = Product.objects.create(name=n, image=i, desc=d,stock=s,price=p,category=cat)  # creates a new record
        a.save()  # saves the record inside the table Book
        return redirect('shop:categories')

    return render(request, 'addproducts.html')

def addstock(request,i):
    p=Product.objects.get(id=i)
    if(request.method=="POST"):
        p.stock = request.POST['s']
        p.save()
        return redirect('shop:detail',i)
    context={'pro':p}
    return render(request,'addstock.html',context)


