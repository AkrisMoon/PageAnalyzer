from django.db import models

class Inquiry(models.Model):
    page = models.URLField(max_length=255)
    result = models.TextField(blank=True)
