from django import template
from cloudinary.utils import cloudinary_url

register = template.Library()

@register.filter(name='cloudinary_thumbnail')
def cloudinary_thumbnail(image_url):
    options = {
        'crop': 'thumb',
        'width': 300,
        'height': 300,
        'format': 'jpg',
        'quality': 'auto'
    }
    thumbnail_url, options = cloudinary_url(image_url, **options)
    return thumbnail_url
