from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.home,name="home"),
    path('view/',views.view,name="view"),
    path('delete/<int:sno>',views.delete,name="delete"),
    path('update/<sno>', views.edit ),
]