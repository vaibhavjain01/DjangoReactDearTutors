from api.models import Test
from rest_framework import viewsets, permissions
from .serializers import TestSerializer

#Test Viewset
class TestViewSet(viewsets.ModelViewSet):
    queryset = Test.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = TestSerializer