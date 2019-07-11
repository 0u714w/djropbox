from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, HttpResponseRedirect
from django.views import View
from djropbox.authentication.forms import LoginForm


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

        return render(request, self.template_name,
                      {'header': self.header, 'form': form,
                       'button_val': self.button_val}
                      )


class LogoutView(View):
    def get(self, request):
        html = 'logout.html'
        logout(request)
        return render(request, html)
