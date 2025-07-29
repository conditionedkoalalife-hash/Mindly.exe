from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('journal/', views.journal_view, name= 'journal'),
    path('affirmations/', views.affirmations_view, name='affirmations'),
    path('connect/', views.connect_view, name='connect'),
    path('register/', views.register_view, name='register'),
]