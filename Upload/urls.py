from .views import FileUploadView,FileFetchView,FileDeleteView
from django.urls import path
urlpatterns = [
    path('file/upload', FileUploadView.as_view()),
    path('files/fetch',FileFetchView.as_view()),
    path('file/delete',FileDeleteView.as_view()),
]