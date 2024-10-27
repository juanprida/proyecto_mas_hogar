from django import template
from cloudinary.utils import cloudinary_url

register = template.Library()

@register.filter(name='cloudinary_thumbnail')
def cloudinary_thumbnail(image_url, width=400, height=400):
    options = {
        'crop': 'fill',
        'width': width,
        'height': height,
        'format': 'jpg',
        'quality': 'auto'
    }
    thumbnail_url, options = cloudinary_url(image_url, **options)
    return thumbnail_url
