from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('order/<str:pk>/', views.order, name="order"),
    path('delivery/', views.delivery, name="delivery"),
    path('details/<int:id>/', views.details, name="details"),
    path('changedestination/', views.changedestination, name="changedestination"),
    # path("", views.incident_list, name="home"),
    path("incident/<str:inc_number>/", views.incident_view, name="incident"),
    path('order/', views.order , name='order'),
]