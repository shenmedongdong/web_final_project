from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('blog/', views.home, name='home'),
    path('blog/search/', views.search, name='search'),
    path("blog/register/", views.register, name="register")
]