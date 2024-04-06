from django.db import models
    
class Projekt(models.Model): 
    title = models.CharField(max_length=200, null=True)
    kurzbeschreibung = models.CharField(max_length=500, null=True)
    content = models.TextField(null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    image_1 = models.ImageField(null=True, blank=True)
    image_2 = models.ImageField(null=True, blank=True)
    image_3 = models.ImageField(null=True, blank=True)
    image_4 = models.ImageField(null=True, blank=True)
    skills = models.CharField(max_length=300, null=True)
    github_link = models.CharField(max_length=300, null=True)
    
    def __str__(self): 
        return str(self.title)

