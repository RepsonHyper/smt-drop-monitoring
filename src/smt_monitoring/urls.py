from django.urls import path
from . import views

app_name = "smt_monitoring"

urlpatterns = [
    path("dashboard/", views.dashboard, name="dashboard"),
]
