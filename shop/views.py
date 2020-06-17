from django.shortcuts import render
from django.http import *
from .models import Product,user
from . import models
# Create your views here.
ls=[]
def index(req):
    products=Product.objects.all()
    n=len(products)
    email = req.POST.get('email', '')
    password = req.POST.get('password', '')
    if email !='' and password!='':
     ls.clear()
     users=user.objects.all()
     for i in users:
        if i.email==email and i.pascode==password:
           ls.append(email)
           ls.append(password)
           break
     else:
         return render(req,'shop/Login.html',{'kal':True})
    params = {'products': products, 'range': list(range(n)),'val':False}
    check = req.POST.get('signout', False)
    if check:
        ls.clear()
    if len(ls)!=0:
        params['val']=True

    return render(req,'shop/shop.html',params)
def aboutus(req):
    op={'val':False}
    if len(ls)!=0:
        op['val']=True
    return render(req,'shop/about.html',op)
def contactus(req):
    return HttpResponse("ok")
def tracker(req):
    return HttpResponse("ok")
def search(req):
    return HttpResponse("ok")
def productview(req):
    return HttpResponse("ok")
def checkout(req):
    all = req.POST.get('all', '')
    obj = models.cart.objects.get(id=all)
    obj.payment = True
    obj.save()
    al = []
    pp = []
    if len(ls) != 0:
        cartob = models.cart.objects.all()
        for i in cartob:
            if i.email == ls[0]:
                for k in Product.objects.all():
                    if k.product_name == i.products and not i.payment:
                        al.append(i)
                        pp.append(k)
                        break
    else:
        return render(req, 'shop/Login.html', {'login': True})

    ziplist=zip(al,pp)
    params = {"val": False, 'cart':ziplist}
    if len(ls) != 0:
        params['val'] = True
    check = req.POST.get('signout', False)
    if check:
        ls.clear()
    return render(req, 'shop/cart.html', params)

def learnmore(req):
    return render(req,'shop/readmore.html')
def Login(req):
    return render(req,'shop/Login.html')
def Signup(req):
    name=req.POST.get('Name','')
    email = req.POST.get('email','')
    password=req.POST.get('password','')
    if name!='' and name and email and email!='' and password and password!='':
     registration = user()
     registration.name=name
     registration.email=email
     registration.pascode=str(password)
     registration.save()
    params={'name':name,'email':email,password:password}
    return render(req,"shop/signup.html",params)
def cart(req):
    products = Product.objects.all()
    n = len(products)
    params = {'products': products, 'range': list(range(n)),'val':False}
    if len(ls) != 0:
        params['val'] = True
    check = req.POST.get('signout', False)
    if check:
            ls.clear()
    if len(ls)!=0:
      users=user.objects.all()
      product=req.POST.get('products','')
      cartpro=models.cart()
      cartpro.email=str(ls[0])
      print(str(ls[0]))
      cartpro.products=product
      cartpro.payment=False
      cartpro.save()
    #vak=req.GET.get('products','')
    #return HttpResponse(str(vak))
    else:
        return render(req,'shop/Login.html',{'login':True})
    return render(req,'shop/shop.html',params)
def cartPage(req):
    al=[]
    pp=[]
    if len(ls)!=0:
        cartob = models.cart.objects.all()
        for i in cartob:
            if i.email==ls[0]:
                for k in Product.objects.all():
                    if k.product_name==i.products and not i.payment:
                        al.append(i)
                        pp.append(k)
                        break
    else:
        return render(req,'shop/Login.html',{'login':True})
    ziplist=zip(al,pp)
    params = {"val":False, 'cart':ziplist}
    if len(ls) != 0:
        params['val'] = True
    check = req.POST.get('signout', False)
    if check:
        ls.clear()
    return render(req,'shop/cart.html',params)
def showall(req):
    pros=Product.objects.all()
    params={'kanx':pros}
    return render(req,'shop/showall.html',params)
