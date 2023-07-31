from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('new', views.new, name='new')
]