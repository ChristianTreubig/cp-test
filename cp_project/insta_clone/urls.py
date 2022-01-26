from django.urls import path, reverse_lazy
from django.conf import settings
from django.contrib.auth.views import LogoutView

from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('sign_up', views.SignupView.as_view(), name='sign_up'),
    path('logout', LogoutView.as_view(), name='logout'),
]