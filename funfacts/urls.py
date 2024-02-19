from . import views
from django.urls import path

urlpatterns = [
    path('', views.FunfactsList.as_view(), name='funfacts'),
]