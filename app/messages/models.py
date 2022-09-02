from django.db import models

class Messages(models.Model):
    content = models.TextField()
    
