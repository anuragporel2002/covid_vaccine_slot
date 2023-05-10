from django.urls import path
from Home import views

urlpatterns = [
    path('',views.home, name='home'),
    path('signup',views.signup,name='signup'),
    path('login',views.loginPage,name='login'),
    path('logout',views.logoutUser,name='logout')
]