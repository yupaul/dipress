from django.contrib import admin
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from dipressapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('list/', views.list_all),
    path('read/<int:pkey>/', views.read),
    path('create/', views.create),
]

urlpatterns = format_suffix_patterns(urlpatterns)
