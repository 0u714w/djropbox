from django.contrib.auth import login
from django.contrib.auth.models import User
from django.shortcuts import render, HttpResponseRedirect, reverse
from django.views import View
from djropbox.user.forms import SignupForm
from djropbox.user.models import BoxUser


def signup_user(request):
    form = None
    html = '../templates/main.html'
    header = 'Signup'
    button_val = 'Signup'

    if request.method == 'POST':
        form = SignupForm(request.POST)

        if form.is_valid():
            data = form.cleaned_data
            user = User.objects.create_user(
                username=data['username'], password=data['password']
            )
            login(request, user)
            BoxUser.objects.create(
                username=data['username'],
                user=user
            )
            return HttpResponseRedirect(reverse('home'))

    else:
        form = SignupForm()

    return render(request, html, {'header': header, 'form': form,
                                  'button_val': button_val})
