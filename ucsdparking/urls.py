from django.urls import path
from . import views

app_name = "ucsdparking"

urlpatterns = [
    path('', views.home_page_view, name='home'),
    path('about', views.info_page_view, name='about'),
    path('usecases', views.usecases_page_view, name='usecases'),
    path('map', views.map_page_view, name='map'),
    path('dashboards', views.dashboard_page_view, name='dashboards'),
    path('dashboards2', views.dashboard2_page_view, name='dashboards2'),
    path('dashboards3', views.dashboard3_page_view, name='dashboards3'),
    path('dashboards4', views.dashboard4_page_view, name='dashboards4'),
    path('dashboards5', views.dashboard5_page_view, name='dashboards5'),
]
