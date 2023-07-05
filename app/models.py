from django.db import models

class Company(models.Model):
    industry_name = models.CharField(max_length=225, null=True, blank=True)
    domain = models.CharField(max_length=225,null=True, blank=True)
    year_founded = models.CharField(max_length=225, null=True, blank=True)
    size_range = models.CharField(max_length=225,null=True, blank=True)
    locality = models.CharField(max_length=225, null=True, blank=True)
    country = models.CharField(max_length=225,null=True, blank=True)
    linkedIn_url = models.CharField(max_length=225, null=True, blank=True)
    current_estimate_emp = models.CharField(max_length=225,null=True, blank=True)
    total_estimate_emp = models.CharField(max_length=225,null=True, blank=True)
    def __str__(self):
        return self.industry_name
