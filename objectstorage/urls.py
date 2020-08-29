from django.urls import path
from object_storage.views import file_upload_view

urlpatterns = [
    path('file_upload', file_upload_view, name='file-upload-view')
]
