from django.urls import path
from . import views

app_name = 'user-urls'

urlpatterns = [
    path('profile/<userid>', views.user_profile, name='user-profile'),
]