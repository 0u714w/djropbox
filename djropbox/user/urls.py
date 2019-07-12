from djropbox.authentication.views import (signup_user)
from django.urls import path

urlpatterns = [
    path('signup/', signup_user),
]
