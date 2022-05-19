from django.db import models
import uuid

class File(models.Model):

    FILE_TYPES = [
        ('video', 'video'),
        ('audio', 'audio'),
        ('image', 'image'),
        ('pdf', 'pdf'),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=1000, blank=False, null=False)
    file_type = models.CharField(max_length=200, blank=False, null=False, default='image', choices=FILE_TYPES)
    image = models.ImageField(upload_to='uploaded_images/', default='uploaded_images/default.jpg')
    file = models.FileField(blank=False, null=False)
    
    def __str__(self):
        return self.name
