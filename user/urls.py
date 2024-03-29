from django.urls import path
from . import views

urlpatterns = [
    path('', views.account, name='account'),
    path('logout/', views.logout_view, name='logout'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('UserUpdate/',views.UserUpdate, name='UserUpdate'),
    path('upload/<int:id>', views.upload, name='upload'),
]

