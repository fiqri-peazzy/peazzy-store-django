from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [
    path('register/',views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('', views.dashboard, name='dashboard'),

    path('activate/<uidb64>/<token>/',views.activate, name='activate'),
    path('forgotpassword/', views.forgotpassword, name='forgotpassword'),
    path('reset-password/<uidb64>/<token>/',views.resetpass_validate, name='resetpass_validate'),
    path('resetPassword/', views.resetPassword, name='resetPassword'),
]