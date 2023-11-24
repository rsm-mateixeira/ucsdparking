from django.urls import path
from . import views

app_name = "ucsdparking"

urlpatterns = [
    path('', views.home_page_view, name='home'),
    path('about', views.info_page_view, name='about'),
    path('map', views.map_page_view, name='map'),
    path('dashboards', views.dashboard_page_view, name='dashboards'),
    path('dashboards2', views.dashboard2_page_view, name='dashboards2'),
]
