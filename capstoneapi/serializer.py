from rest_framework import serializers

from .models import JobApplication, PotentialEmployee

class JobApplicationSerializer(serializers.ModelSerializer):
    # metadata that describes the model and what fields will be returned
    class Meta:
        model = JobApplication
        fields = ['id', 'jobName', 'jobDescription', 'desiredSkills', 'minGPA', 'location', 'pastExperiences', 'aptitudeResultsMin', 'applicants', 'date']

class PotentialEmployeeSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = PotentialEmployee
        fields = ['name', 'skills', 'GPA', 'location', 'pastExperiences', 'aptitudeResults', 'jobApplication']