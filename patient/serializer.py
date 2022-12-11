from .models import Patient, Exam
from rest_framework.serializers import ModelSerializer


class PatientSerializer(ModelSerializer):
    class Meta:
        model = Patient
        fields = '__all__'


class ExamSerializer(ModelSerializer):
    class Meta:
        model = Exam
        fields = '__all__'
