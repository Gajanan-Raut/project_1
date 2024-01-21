from django.contrib import admin
from django.urls import path
from shoppingapp import views

urlpatterns = [
    path('home',views.home),
    path('index',views.index),
    path('base',views.base),
    path('evenodd/<n>',views.evenodd),
    path('edit/<n>',views.edit),
    path('about',views.about),
    path('create_task',views.create_task),
    path('delete/<d>',views.delete),
    path('dashboard',views.dashboard),
    path('cdashboard',views.cdashboard),
    path('deleted/<n>',views.deleted),
    path('edits/<n>',views.edits),
    path('ltoh',views.lowtohigh),
    path('htol',views.hightolow),
    path('forms',views.emps),
    path('studs',views.studs),
    path('cform',views.stude),
    path('cview',views.cview.as_view()),
    path('register',views.resiter),
    path('navbar',views.navbar)
]