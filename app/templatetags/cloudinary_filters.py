from django import template
from cloudinary.utils import cloudinary_url

register = template.Library()

@register.filter(name='cloudinary_thumbnail')
def cloudinary_thumbnail(cloudinary_field):
    options = {
        'crop': 'fill',          # Crop the image to fill the dimensions
        'gravity': 'auto',       # Focus on the important part of the image
        'width': 500,
        'height': 500,
        'format': 'jpg',
        'quality': 'auto'
    }
    public_id = cloudinary_field.public_id
    thumbnail_url, _ = cloudinary_url(public_id, **options)
    return thumbnail_url
