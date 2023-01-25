from django.urls import path

from . import views

urlpatterns = [
    # path('', view, name=""),
    path('login', views.Userlogin, name="login"),
    path('register', views.register, name="register"),
]
