from django.urls import path
from .views import HomePage,Register,Login

urlpatterns = [
    path('home/', HomePage,name="home-page"),
    path('register/',Register,name="register-page"),
    path('login/',Login,name="login-page")
]