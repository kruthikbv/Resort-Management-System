from django.contrib import admin
from django.urls import path,include
from resortbkdapp import views
urlpatterns = [

    path('admin/', admin.site.urls),
    path('',views.SignupPage,name='signup'),
    path('login/',views.LoginPage,name='login'),
    path('home/',views.home,name='home'),
    path('logout/',views.LogoutPage,name='logout'),
    path('',include('resortbkdapp.urls')),
] 
