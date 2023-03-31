from django.urls import path
from . import views

app_name = 'menu'

urlpatterns = [
    path('menu/', views.TemplateView.as_view(), name='index'),
]
