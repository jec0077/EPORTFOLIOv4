from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('projects/', views.projects, name="projects"),
	path('live-resume/', views.live_resume, name="resume"),
	path('career/', views.career, name="career"),
	path('contact/', views.contact, name="contact")
]
