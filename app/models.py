from cloudinary.models import CloudinaryField
from django.db import models


class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.title


class ProjectImage(models.Model):
    project = models.ForeignKey(Project, related_name="images", on_delete=models.CASCADE)
    image = CloudinaryField("image")  # Store the image in Cloudinary

    def __str__(self):
        return self.project.title
