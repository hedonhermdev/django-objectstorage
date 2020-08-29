from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save

# Create your models here.

class MediaObject(models.Model):
    """
    Stores in the database, the attributes of each file stored in the object storage. 
    """
    name = models.CharField(max_length=1024, null=True)
    hashed_name = models.CharField(max_length=50, primary_key=True)
    url = models.CharField(max_length=1024, null=True)

    def __str__(self):
        return f"MediaObject({self.name, self.sha1_hash})"

# Create your models here.
