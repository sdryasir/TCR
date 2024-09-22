from PIL import Image
from django.core.exceptions import ValidationError

def validate_image_dimensions(image):
    # Define the maximum allowed dimensions
    max_width = 1920
    max_height = 700

    # Open the image file
    img = Image.open(image)
    width, height = img.size

    # Check the image dimensions
    if width > max_width or height > max_height:
        raise ValidationError(f'Image dimensions should not exceed {max_width}x{max_height} pixels. '
                              f'Your image is {width}x{height} pixels.')