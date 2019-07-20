from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, HttpResponseRedirect
from django.views import View
from djropbox.authentication.forms import LoginForm
from django.contrib.auth.decorators import login_required
from djropbox.file_uploader.models import Folder, NewFile
from djropbox.user.models import BoxUser


class LoginView(View):
    form_class = LoginForm
    template_name = '../templates/main.html'
    header = 'Login'
    button_val = 'Login'
    url_redirect = '/'

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name,
                      {'header': self.header, 'form': form,
                       'button_val': self.button_val}
                      )

    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(
                username=data['username'], password=data['password'])

            if user is not None:
                login(request, user)
                return HttpResponseRedirect(request.GET.get('next', '/'))
            
            else:
                messages.info(request, 'Username and/or password do not match')
                return HttpResponseRedirect('/login')

        return render(request, self.template_name,
                      {'header': self.header, 'form': form,
                       'button_val': self.button_val}
                      )


class LogoutView(View):
    def get(self, request):
        html = 'index.html'
        logout(request)
        return render(request, html)

@login_required()
def profile_view(request):
    print(request.user.boxuser)
    user = request.user
    djropbox_user = request.user.boxuser.username
    myfolder_list = Folder.objects.filter(creator=request.user.boxuser)
    object_list = NewFile.objects.all()
    homefolder = Folder.objects.filter(creator=request.user.boxuser).filter(name='home').first()
    potentialfolder = Folder.objects.filter(creator=request.user.boxuser).filter(name='home').first()
    data = {
        'currentfolder': potentialfolder,
        'files': NewFile.objects.filter(folder=potentialfolder),
        'children': potentialfolder.get_children(),
    }
    print(potentialfolder)

    context = {
        'DjropboxUser': BoxUser,
        'user': user,
        'Djropbox_user': djropbox_user,
        'object_list': object_list,
        'data': data,
        'homefolder': homefolder,
    }
    return render(request, 'profile.html', context)

@login_required()
def folder_view(request, id):
    user = request.user
    folder_list = Folder.objects.all()
    myfolder_list = Folder.objects.filter(creator=request.user.boxuser)
    object_list = NewFile.objects.all()
    potentialfolder = Folder.objects.filter(creator=request.user.boxuser).filter(id=id).first()
    data = {
       'currentfolder': potentialfolder,
       'files': NewFile.objects.filter(folder=potentialfolder),
       'children': potentialfolder.get_children(),
    }

    structure = {
        'documents': data['files']

    }

    context = {
        'DjropboxUser': BoxUser,
        'user': user,
        'data': data,
        'structure': structure
    }
    return render(request, 'folder.html', context)


def success_view(request):
    return render(request, 'success.html')


def handler404(request, exception):
    return render(request, '404.html', status=404)


def handler500(request):
    return render(request, '500.html', status=500)
