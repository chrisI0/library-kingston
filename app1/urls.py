from django.urls import path
from . import views

urlpatterns = [
    path('home', views.home, name='home'),
    path('about', views.about, name='about'),
    path('admin', views.adm_login, name='admin'),
     path('admin_logout', views.adm_logout, name='admin_logout'),
    path('bookentry', views.bookentry, name='bookentry'),
    path('books', views.c_admin, name='books'),
    path('borrow', views.borrow1, name='borrow'),
    path('borrowed', views.borrowed, name='borrowed'),
     path('return_book', views.return_book, name='return_book'), # New path
]