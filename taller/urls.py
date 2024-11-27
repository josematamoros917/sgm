# taller/urls.py
from django.urls import path
from .views import TallerPageView

urlpatterns = [
    path('', TallerPageView.as_view(), name='taller_page'),
]
