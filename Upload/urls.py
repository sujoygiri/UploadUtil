from .views import FileUploadView,FileFetchView
from django.urls import path
urlpatterns = [
    path('files/upload', FileUploadView.as_view()),
    path('files/fetch',FileFetchView.as_view()),
]