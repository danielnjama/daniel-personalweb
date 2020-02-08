from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('',views.index,name='index'),
    path('contacts',views.contacts, name='contacts'),
    path('services',views.myservices,name='myservices'),
    path('testimonials',views.mytestimonials,name='testimonials'),
    #path('blog',views.blog,name='blog'),
    path("accounts/register",views.register, name="register"),
    path('blog',views.blog,name='blog'),
]
