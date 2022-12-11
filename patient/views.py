from rest_framework.viewsets import ModelViewSet

from .models import (
    Patient,
    Exam,
)
from .pagination import StandardResultsSetPagination
from .serializer import PatientSerializer, ExamSerializer


class PatientModelViewSet(ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
    pagination_class = StandardResultsSetPagination


class ExamModelViewSet(ModelViewSet):
    queryset = Exam.objects.all()
    serializer_class = ExamSerializer
    pagination_class = StandardResultsSetPagination
