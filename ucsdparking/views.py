from django.shortcuts import render

# Create your views here.

def home_page_view(request):
    return render(request, 'ucsdparking/home.html')

def info_page_view(request):
    return render(request, 'ucsdparking/info.html')

def dashboard_page_view(request):
    return render(request, 'ucsdparking/dashboard.html')


