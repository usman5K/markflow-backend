from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import ListAPIView

from .models import Document, Tag
from .serializers import DocumentSerializer


class DocumentViewSet(viewsets.ModelViewSet):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        request.data["created_by"] = self.request.user
        return super().create(request, *args, **kwargs)


    def get_queryset(self):
        if self.request.user.is_authenticated:
            return Document.objects.filter(created_by=self.request.user)
        return Document.objects.none()


class ListTags(ListAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Tag.objects.all()