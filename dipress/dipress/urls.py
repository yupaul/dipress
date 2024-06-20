from django.contrib import admin
from django.urls import path
from . import views as views_index
from rest_framework.urlpatterns import format_suffix_patterns
from dipressapp import views

urlpatterns = [
    path('', views_index.index, name='index'),
    path('admin/', admin.site.urls),
    path('list/', views.list_all),
    path('read/<int:pkey>/', views.read),
    path('create/', views.create),  
]

urlpatterns = format_suffix_patterns(urlpatterns)
