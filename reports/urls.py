from django.urls import path
from . import views 

app_name = "reports"

urlpatterns = [
    path('', views.main, name='reports_list'),
]