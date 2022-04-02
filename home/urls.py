from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('order/<str:pk>/', views.order, name="order"),
    path('delivery/', views.delivery, name="delivery"),
    path('details/', views.details, name="details"),
    path('changedestination/', views.changedestination, name="changedestination"),
    path('order/', views.order , name='order'),
]