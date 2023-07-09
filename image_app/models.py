from django.contrib.auth.models import User
from django.db import models

class Image(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)  # Set a default value here
    title = models.CharField(max_length=255)
    image_data = models.BinaryField()
    created_at = models.DateTimeField(auto_now_add=True)
