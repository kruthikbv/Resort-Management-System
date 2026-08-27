from django.urls import path
from . import views

urlpatterns = [
    #path('', views.home, name='home'),
    path('conv/', views.conv, name='conv'),
    path('food/', views.food, name='food'),
    path('gallery/', views.gallery, name='gallery'),
    path('expeditions/', views.expeditions, name='expeditions'),
    path('lq/', views.lq, name='lq'),
    path('submit/', views.submit, name='submit'),
    #dropdown
    path('reserve/',views.reserve,name='reserve'),
    path('venue/',views.venue,name='venue'),
    path('roombooking/',views.roombooking,name='roombooking'),
    path('payment/',views.payment,name='payment'),
    path('bs/',views.bs,name='bs'),
    path('contact',views.contact,name='contact'),
    
]
