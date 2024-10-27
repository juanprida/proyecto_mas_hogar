from django import template
from cloudinary.utils import cloudinary_url

register = template.Library()

@register.filter(name='cloudinary_thumbnail')
def cloudinary_thumbnail(image_url):
    options = {
        'crop': 'fill',
        'width': 400,
        'height': 400,
        'format': 'jpg',
        'quality': 'auto'
    }
    thumbnail_url, options = cloudinary_url(image_url, **options)
    return thumbnail_url
