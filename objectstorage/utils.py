import hashlib
from django.core.files import File

def calculate_sha1_hash(data: bytes) -> str:
    """
    Given a django file, calculate its hash
    """
    hasher = hashlib.sha1()
    hasher.update(data.read())

    return hasher.hexdigest()

