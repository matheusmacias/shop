from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name="home_page"),
    path('produto/<str:url_produto>', views.produto, name='url_produto'),
]
