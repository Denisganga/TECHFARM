from django.urls import path

from django.contrib.auth import views as auth_views

from .views import HomePage,Register,Login

urlpatterns = [
    path('home/', HomePage,name="home-page"),
    path('register/',Register,name="register-page"),
    path('login/',Login,name="login-page"),

    path('reset_password/',
          auth_views.PasswordResetView.as_view(template_name="auth_system/password_reset.html"),
            name= "reset_password"),

    path('reset_password_sent/', 
         auth_views.PasswordResetView.as_view(template_name="auth_system/password_reset_sent.html"), 
         name="password_reset_done"),

    path('reset/<uidb64>/<token>/', auth_views.PasswordResetView.as_view(), name= "password_reset_confirm"),

    path('reset_password_complete/', 
         auth_views.PasswordResetView.as_view(template_name="auth_system/password_reset_done.html"), 
         name="password_reset_complete"),
    
    ]