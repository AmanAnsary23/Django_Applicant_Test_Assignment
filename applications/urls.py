from django.urls import path
from . import views

urlpatterns = [
    # Applicant endpoints
    path('applicants/', views.ApplicantListCreateView.as_view(), name='applicant-list'),
    path('applicants/<int:pk>/', views.ApplicantDetailView.as_view(), name='applicant-detail'),
    
    # Job endpoints
    path('jobs/', views.JobListCreateView.as_view(), name='job-list'),
    path('jobs/<int:pk>/', views.JobDetailView.as_view(), name='job-detail'),
    
    # Application endpoints
    path('apply/', views.apply_for_job, name='apply-job'),
    path('applications/', views.ApplicationListView.as_view(), name='application-list'),
    path('applications/<int:pk>/', views.update_application_status, name='update-application-status'),
]