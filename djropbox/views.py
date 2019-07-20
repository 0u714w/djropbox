from django.shortcuts import render


def index(request):
    html = "index.html"
    return render(request, html)


def handler404(request):
    return render(request, '404.html', status=404)


def handler500(request):
    return render(request, '500.html', status=500)
