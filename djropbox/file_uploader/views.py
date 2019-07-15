from django.shortcuts import render
from djropbox.file_uploader.models import Folder, NewFile
from djropbox.file_uploader.forms import Add_File, Add_Folder
from django.views import View

class FolderView(View):
    folder_form = Add_Folder
    initial = {'key': 'value'}
    html = 'form.html'

    def get(self, request):
        form = self.folder_form(request.user.boxuser, initial=self.initial)
        return render(request, self.html, {'form': form})

    def post(self, request):
        form = self.folder_form(request.user.boxuser, request.POST)

        if form.is_valid():
            data = form.cleaned_data
            folder = Folder.objects.create(
                parent=data['parent'],
                name=data['name'],
                creator=request.user.boxuser)
            return render(request, 'success.html')
        else:
            form = Add_Folder

        return render(request, self.html, {'form': form})


class FileView(View):
    file_form = Add_File
    initial = {'key': 'value'}
    html = 'fileform.html'

    def get(self, request):
        form = self.file_form(request.user.boxuser, initial=self.initial)
        return render(request, self.html, {'form': form})

    def post(self, request):
        form = self.file_form(request.user.boxuser, request.POST, request.FILES)
        if form.is_valid():
            data = form.cleaned_data
            file_object = NewFile.objects.create(
                folder=data['folder'],
                name=data['name'],
                document=request.FILES['document'])
            return render(request, 'success.html')
        else:
            form = Add_File
        return render(request, self.html, {'form': form})
