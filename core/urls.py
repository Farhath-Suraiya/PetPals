from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('pets/', views.pets, name='pets'),
    path('pets/<int:pet_id>/', views.pet_detail, name='pet_detail'),
    path('favorites/', views.favorites, name='favorites'),
    path('favorites/add/<int:pet_id>/', views.add_favorite, name='add_favorite'),
    path('favorites/remove/<int:pet_id>/', views.remove_favorite, name='remove_favorite'),
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
]
