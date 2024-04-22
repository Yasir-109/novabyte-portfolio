from django.db import models

# Create your models here.

class Project(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    url = models.URLField()
    image = models.ImageField(upload_to='portfolio/images/')
    date_uploaded = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
