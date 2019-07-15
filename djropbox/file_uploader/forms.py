from django import forms
from mptt.forms import TreeNodeChoiceField
from djropbox.file_uploader.models import Folder, NewFile


class Add_Folder(forms.Form):
    def __init__(self, user, *args, **kwargs):
        super(Add_Folder, self).__init__(*args, **kwargs)
        # init will run more than once, but the first time that it runs the
        # fields attribute will not be present
        try:
            self.fields['parent'].queryset = Folder.objects.filter(creator=user)
        except AttributeError:
            pass

    parent = TreeNodeChoiceField(queryset=Folder.objects.all())
    name = forms.CharField(max_length=60)

def get_folder_structure(request):
    return Folder.objects.filter(
        creator=request.user.boxuser
        ).filter(name='home').get_descendants(include_self=True)

class Add_File(forms.Form):
    def __init__(self, request, *args, **kwargs):
        super(Add_File, self).__init__(*args, **kwargs)
        # init will run more than once, but the first time that it runs the
        # fields attribute will not be present
        try:
            self.fields['folder'].queryset = get_folder_structure(request)

        except AttributeError:
            pass

    folder = TreeNodeChoiceField(queryset=Folder.objects.all())
    document = forms.FileField(label='select a file')
    name = forms.CharField(max_length=60)