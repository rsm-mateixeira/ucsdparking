from django.shortcuts import render

# Create your views here.

def home_page_view(request):
    return render(request, 'ucsdparking/home.html')

def info_page_view(request):
    return render(request, 'ucsdparking/info.html')

def map_page_view(request):
    return render(request, 'ucsdparking/map.html')

def dashboard_page_view(request):
    return render(request, 'ucsdparking/dashboard.html')

def dashboard2_page_view(request):
    return render(request, 'ucsdparking/dashboard2.html')

def dashboard3_page_view(request):
    return render(request, 'ucsdparking/dashboard3.html')

def dashboard4_page_view(request):
    return render(request, 'ucsdparking/dashboard4.html')

def dashboard5_page_view(request):
    return render(request, 'ucsdparking/dashboard5.html')