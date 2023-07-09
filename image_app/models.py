from django.db import models

class Image(models.Model):
    title = models.CharField(max_length=255)
    image_data = models.BinaryField()
    created_at = models.DateTimeField(auto_now_add=True)
