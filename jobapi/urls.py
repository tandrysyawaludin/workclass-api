from django.urls import path
from . import views

urlpatterns = [
	path('', views.apiOverview, name="api-overview"),
	path('job-list', views.jobList, name="job-list"),
	path('job-create/', views.jobCreate, name="job-create"),
	path('job-update/<str:pk>/', views.jobUpdate, name="job-update"),
	path('job-delete/<str:pk>/', views.jobDelete, name="job-delete"),
]
