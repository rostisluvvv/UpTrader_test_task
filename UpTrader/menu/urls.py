from django.urls import path
from . import views

app_name = 'menu'

urlpatterns = [
    path('', views.index_menu_page, name='index'),
    path('<slug:slug>/', views.single_menu_page, name='menu'),
]
