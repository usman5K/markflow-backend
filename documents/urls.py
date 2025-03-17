from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import DocumentViewSet, ListTags

router = DefaultRouter()
router.register(r'documents', DocumentViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('tags/', ListTags.as_view(), name='list_tags'),
]
