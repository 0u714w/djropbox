"""djropbox URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from djropbox.views import index

from djropbox.file_uploader.models import Folder, NewFile
from djropbox.file_uploader.views import FolderView, FileView
from djropbox.user.models import BoxUser
from djropbox.authentication.views import LoginView, LogoutView, profile_view, folder_view, success_view
from djropbox.user.views import signup_user
from django.conf.urls.static import static
from django.conf import settings

admin.site.register(BoxUser)
admin.site.register(Folder)
admin.site.register(NewFile)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('login/', LoginView.as_view()),
    path('logout/', LogoutView.as_view()),
    path('signup/', signup_user),
    path('profile/', profile_view),
    path('add_folder/', FolderView.as_view()),
    path('folder/<int:id>', folder_view),
    path('add_file/', FileView.as_view()),
    path('success/', success_view)
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
