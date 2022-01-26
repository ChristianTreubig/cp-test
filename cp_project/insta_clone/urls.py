from django.urls import path, reverse_lazy
from django.conf import settings
from django.contrib.auth.views import LogoutView

from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('profile/<int:profile_user_id>/', views.profile, name='profile'),
    path('follow/<int:profile_user_id>/', views.follow, name='follow'),
    path('unfollow/<int:profile_user_id>/', views.unfollow, name='unfollow'),
    path('search_users', views.search_users, name='search_users'),
    path('photo_upload', views.PhotoUploadView.as_view(), name='photo_upload'),
    path('sign_up', views.SignupView.as_view(), name='sign_up'),
    path('logout', LogoutView.as_view(), name='logout'),
]
