from django.urls import path
from . import views

app_name = "ucsdparking"

urlpatterns = [
    path('', views.home_page_view, name='home'),
    path('info', views.info_page_view, name='info'),
    path('dashboards', views.dashboard_page_view, name='dashboards'),
]
