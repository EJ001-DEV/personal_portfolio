from django.db import models
import datetime
from django.db.models.fields import URLField

class Post(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='blog/images')
    date = models.DateField(datetime.date.today)
    url = URLField(blank=True)
    pdf_1 = models.FileField(upload_to='pdfs/', null=True, blank=True)
    pdf_2 = models.FileField(upload_to='pdfs/', null=True, blank=True)