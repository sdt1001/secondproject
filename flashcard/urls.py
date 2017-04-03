"""flashcard URL Configuration copied from ustudy urls.py
"""
from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^', views.home, name='home'),
]
