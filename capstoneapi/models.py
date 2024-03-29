from django.contrib.postgres.fields import ArrayField
from django.db import models
from datetime import date

class JobApplication(models.Model):
    jobName = models.CharField(max_length=300)
    jobDescription = models.CharField(max_length=1000)
    desiredSkills = models.JSONField()
    minGPA = models.DecimalField(decimal_places=2, max_digits=3, null=True)
    location = models.CharField(max_length=150)
    pastExperiences = models.JSONField()
    aptitudeResultsMin = models.IntegerField()
    date = models.DateField(auto_now=True)
    company = models.CharField(max_length=300, default='placeholder_company')
    createdBy = models.CharField(max_length=30, default='placeholder_createdBy')
    aptitudeTest = models.JSONField(default='placeholder_aptitudeTest')
    
    @property
    def applicants(self):
        return PotentialEmployee.objects.filter(jobApplication=self).values()

    def __str__ (self):
        return self.jobName + ' : ' + self.location

class PotentialEmployee(models.Model):
    jobApplication = models.ForeignKey(JobApplication, on_delete=models.CASCADE, default="", null=True)
    name = models.CharField(max_length=300)
    skills = ArrayField(models.CharField(max_length=50))
    GPA = models.DecimalField(decimal_places=2, max_digits=3, null=True)
    location = models.CharField(max_length=150, null=True, blank=True)
    pastExperiences = ArrayField(models.CharField(max_length=100), null=True)
    aptitudeResults = models.IntegerField(null=True)
    email = models.EmailField(max_length=254, default='placeholder_email')
    phoneNumber = models.CharField(max_length=30, blank=True, default='placeholder_number')
    uID = models.CharField(max_length=30, default='placeholder_uID')

    def __str__ (self):
        return self.name + ' : ' + self.location
    