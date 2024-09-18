from django.db import models
import uuid

class LongVideo(models.Model):
    title = models.CharField(max_length=500, blank=True)
    description = models.CharField(max_length=500, blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True, blank=True)
    video_file = models.FileField(upload_to='long_videos/', blank=True)
    outsource_url = models.CharField(max_length=2000, blank=True)
    frontend_uid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)

    STATUS_CHOICES = [
        ('None', 'None'),
        ('Uploaded', 'Uploaded'),
        ('Processing', 'Processing'),
        ('Processed', 'Processed'),
    ]

    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='None')
