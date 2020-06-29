from datetime import datetime
from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Tag(models.Model):
    fromTag = models.ForeignKey(User, on_delete=models.CASCADE, related_name="tags")
    toTag = models.ForeignKey(User, on_delete=models.CASCADE, related_name="taggedBy")
    message = models.CharField(max_length=256, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        if (len(self.message) > 0):
            return f"{self.fromTag} tagged {self.toTag} at {self.timestamp} | {self.message}"
        else:
            return f"{self.fromTag} tagged {self.toTag} at {self.timestamp}"

class TagForm(Tag):
    fromTag = Tag.fromTag
    toTag = Tag.toTag
    message = Tag.message
    timestamp = datetime.now()