from django.db import models
from PIL import Image
from PIL.Image import Resampling
import os


class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.title


class ProjectImage(models.Model):
    project = models.ForeignKey(Project, related_name="images", on_delete=models.CASCADE)
    image = models.ImageField(upload_to="project_images/")
    thumbnail = models.ImageField(upload_to="project_images/thumbnails/", editable=False, null=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.create_thumbnail()

    def create_thumbnail(self):
        if not self.image:
            return

        # Open the original image
        img = Image.open(self.image.path)
        img = img.convert("RGB")  # Ensure image is in RGB format

        # Set thumbnail size (width, height)
        thumbnail_size = (400, 300)

        # Calculate aspect ratio and crop to fit
        img_ratio = img.width / img.height
        target_ratio = thumbnail_size[0] / thumbnail_size[1]

        if img_ratio > target_ratio:
            # Crop the sides
            new_width = int(img.height * target_ratio)
            left = (img.width - new_width) / 2
            img = img.crop((left, 0, left + new_width, img.height))
        else:
            # Crop the top and bottom
            new_height = int(img.width / target_ratio)
            top = (img.height - new_height) / 2
            img = img.crop((0, top, img.width, top + new_height))

        # Resize the image using Resampling.LANCZOS
        img = img.resize(thumbnail_size, Resampling.LANCZOS)

        # Prepare the thumbnail filename
        base, ext = os.path.splitext(self.image.name)
        thumbnail_name = f"{base}_thumbnail{ext}"
        thumbnail_path = os.path.join("media", thumbnail_name)

        # Save the thumbnail image
        img.save(thumbnail_path)

        # Update the thumbnail field
        self.thumbnail = thumbnail_name
        super().save(update_fields=["thumbnail"])
