from django.urls import path

from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('login/',views.login,name='login'),
    path('signup/',views.registration,name='registration'),
    path('<int:pro_id>/',views.details,name='details'),
    path('allproducts/',views.allpro,name='allproducts'),
    path('<slug:c_slug>/',views.home,name='prod_cat'),
    path('search',views.searching,name="search")

]