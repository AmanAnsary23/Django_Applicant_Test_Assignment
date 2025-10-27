from django.contrib import admin
from .models import Applicant, Job, Application

@admin.register(Applicant)
class ApplicantAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone', 'applied_on']
    search_fields = ['name', 'email']

@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ['title', 'posted_on']
    search_fields = ['title']

@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ['applicant', 'job', 'status', 'applied_on']
    list_filter = ['status', 'applied_on']
    search_fields = ['applicant__name', 'job__title']