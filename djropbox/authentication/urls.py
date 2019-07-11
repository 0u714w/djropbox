from djropbox.authentication.views import (LoginView, LogoutView)
from django.urls import path

urlpatterns = [
    path('login/', LoginView.as_view()),
    path('logout/', LogoutView.as_view())
]
