from django.db import models

# Create your models here.

class Project(models.Model):
    class Category(models.TextChoices):
        PYTHON = 'Python', 'Python'
        DOTNET = 'dot net', 'dot net'
        SEO = 'SEO', 'SEO'


    name = models.CharField(max_length=100)
    description = models.TextField()
    url = models.URLField()
    image = models.ImageField(upload_to='images/')
    date_uploaded = models.DateTimeField(auto_now_add=True)
    category = models.CharField(max_length=20, choices=Category.choices)

    def __str__(self):
        return self.name
    
class ProjectTags(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    tag = models.CharField(max_length=50)

    def __str__(self):
        return self.tag