from django.db import models

# Create your models here.

class Job(models.Model):
  job_id = models.AutoField(primary_key=True)
  company_name = models.CharField(max_length=1000)
  job_title = models.CharField(max_length=1000)
  logo_url = models.CharField(max_length=1000)
  date = models.DateField()