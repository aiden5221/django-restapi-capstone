from django.contrib.postgres.fields import ArrayField
from django.db import models
from datetime import date
class JobApplication(models.Model):
    jobName = models.CharField(max_length=300)
    jobDescription = models.CharField(max_length=1000, default='default job description')
    desiredSkills = models.JSONField()
    minGPA = models.DecimalField(decimal_places=2, max_digits=3)
    location = models.CharField(max_length=150)
    pastExperiences = models.JSONField()
    aptitudeResultsMin = models.DecimalField(decimal_places=2, max_digits=3)
    date = models.DateField(auto_now=True)

    @property
    def applicants(self):
        return PotentialEmployee.objects.filter(jobApplication=self).values()

    def __str__ (self):
        return self.jobName + ' : ' + self.location

class PotentialEmployee(models.Model):
    jobApplication = models.ForeignKey(JobApplication, on_delete=models.CASCADE, default="")
    name = models.CharField(max_length=300)
    skills = ArrayField(models.CharField(max_length=50))
    GPA = models.DecimalField(decimal_places=2, max_digits=3)
    location = models.CharField(max_length=150)
    pastExperiences = ArrayField(models.CharField(max_length=100))
    aptitudeResults = models.DecimalField(decimal_places=2, max_digits=3)

    def __str__ (self):
        return self.name + ' : ' + self.location