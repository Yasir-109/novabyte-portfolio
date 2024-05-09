from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # home page
    path('about/', views.about, name='about'),  # about page
    path('contact/', views.contact, name='contact'),  # contact page
    path('projects/', views.projects, name='projects'),  # projects page
    path('project/<int:pk>/', views.project, name='project'),  # project detail page
    path('contact/submit/', views.contact_submit, name='contact_submit'),
]
