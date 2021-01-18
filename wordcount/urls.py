from django.contrib import admin
from django.urls import path

# from current directory import views.py
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # path and the file of the html(here python file and its function)
    path('', views.home, name='home'),
    # name here is acting as reference in form action
    path('countwords/', views.count, name='count'),
    path('aboutus/', views.aboutus, name='aboutus')
]
