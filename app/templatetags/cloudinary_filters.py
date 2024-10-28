from django import template
from cloudinary.utils import cloudinary_url

register = template.Library()

@register.filter(name='cloudinary_thumbnail')
def cloudinary_thumbnail(image_url):
    options = {
        'crop': 'scale',
        'width': 500,
        'height': 500,
        'format': 'jpg',
        'quality': 'auto'
    }
    thumbnail_url, options = cloudinary_url(image_url, **options)
    return thumbnail_url
