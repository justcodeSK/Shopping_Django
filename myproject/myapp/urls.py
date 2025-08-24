from django.urls import path
from myapp import views


urlpatterns = [
   path('',views.home,name="home"),
   path('reg',views.reg,name="reg"),
   path('login',views.login,name="login"),
   path('logout',views.logout,name="logout"),
   path('us',views.user,name="user"),
   path('acrt/<int:uid>',views.addcart,name="addcart"),
   path('crt',views.cart,name="cart"),
   path('crtdel/<int:uid>',views.cartdel,name="cartdel"),
   path('adm',views.admin,name="admin"),
   path('prdadm',views.productadm,name="productadm"),
   path('upd/<int:uid>',views.update,name="update"),
   path('del/<int:uid>',views.delete,name="delete"),

] 
