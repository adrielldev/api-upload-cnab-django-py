

from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('upload/',views.FileView.as_view())
]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)