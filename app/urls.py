from django.urls import path
from . import views

urlpatterns = [
    path('rv/', views.signupView, name='signup_url'),
    path('', views.loginView, name='loginview_url'),
    path('lot/', views.logoutView, name='logout_url'),
    path('upload/', views.upload, name='upload'),
    path('users/', views.userView, name='users'),
    path('filter/', views.filter_records, name='filter'),

]