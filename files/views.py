from rest_framework.generics import CreateAPIView
from .models import File
from .serializers import FileSerializer
from rest_framework.parsers import MultiPartParser, FormParser

class FileView(CreateAPIView):
    queryset = File.objects.all()
    serializer_class = FileSerializer
    parser_classes = (MultiPartParser, FormParser)