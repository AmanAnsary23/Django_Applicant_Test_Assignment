from rest_framework import serializers
from .models import Applicant, Job, Application

class ApplicantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Applicant
        fields = ['id', 'name', 'email', 'phone', 'resume', 'applied_on']

class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = ['id', 'title', 'description', 'posted_on']

class ApplicationSerializer(serializers.ModelSerializer):
    applicant_name = serializers.CharField(source='applicant.name', read_only=True)
    job_title = serializers.CharField(source='job.title', read_only=True)
    
    class Meta:
        model = Application
        fields = ['id', 'applicant', 'applicant_name', 'job', 'job_title', 'status', 'applied_on']

class ApplicationCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = ['applicant', 'job']

    def validate(self, data):
        applicant = data['applicant']
        job = data['job']
        
        # Check for duplicate application
        if Application.objects.filter(applicant=applicant, job=job).exists():
            raise serializers.ValidationError("You have already applied for this job.")
        
        return data

class ApplicationStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = ['status']