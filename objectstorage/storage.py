from storages.backends.s3boto3 import S3Boto3Storage
from django.core.files.storage import Storage
from objectstorage.models import MediaObject
from objectstorage.utils import calculate_sha1_hash


class S3MediaStorage(S3Boto3Storage):
    location = 'media'
    file_overwrite = False

    def save(self, name, content, max_length=None):
        extension = name.split(".")[-1]
        sha1_hash = calculate_sha1_hash(content)
        hashed_name = sha1_hash + "." + extension
        print(hashed_name)
        try:
            obj = MediaObject.objects.get(hashed_name=hashed_name)
            return obj.hashed_name
        except MediaObject.DoesNotExist:
            return super().save(hashed_name, content, max_length)
