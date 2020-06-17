from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name='shophome'),
    path('aboutus',views.aboutus,name='aboutus'),
    path('contactus',views.contactus,name='contactus'),
    path('tracker',views.tracker,name='tracker'),
    path('search',views.search,name='search'),
    path('productview',views.productview,name='productview'),
    path('checkout', views.checkout, name='checkout'),
    path('readmore',views.learnmore,name='readmore'),
    path('Login',views.Login,name='Login'),
    path('signup',views.Signup,name='signup'),
    path('cart',views.cart,name='cart'),
    path('cpage',views.cartPage,name='cpage'),
    path('showall',views.showall,name='showall')
]
