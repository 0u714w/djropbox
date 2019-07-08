from django.shortcuts import render

def index(request):
    html = "index.html"
    return render(request, html)