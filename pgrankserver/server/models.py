from django.db import models

# Create your models here.

class Website(models.Model):
    url = models.TextField(max_length=100)
    title = models.TextField(max_length=100)
    sample_content = models.TextField(max_length=250)