from django.urls import path, include
from . import views

app_name = 'estoque'

urlpatterns = [
    path('',views.LoginView.as_view(),name = 'login'),
    path('home/',views.HomeView.as_view(),name = 'home')
]