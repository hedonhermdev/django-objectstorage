from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http.response import HttpResponse
# Create your views here.
from django.core.files import File
from django.core.files.storage import default_storage, FileSystemStorage
from objectstorage.utils import calculate_sha1_hash
from objectstorage.models import MediaObject

@csrf_exempt
def file_upload_view(request):
    for name in request.FILES:
        file = request.FILES[name]
        name = file.name

        obj = MediaObject(name=name)

        hashed_name = default_storage.save(name, file)
        print(hashed_name)
        obj.hashed_name = hashed_name

        url = default_storage.url(hashed_name)
        obj.path_or_url = url

        obj.save()

    return HttpResponse(content="File successfully uploaded")


# Create your views here.
