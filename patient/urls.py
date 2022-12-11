from django.urls import path, include
from rest_framework import routers

from .views import PatientModelViewSet, ExamModelViewSet

router = routers.DefaultRouter()
router.register(r'patient', PatientModelViewSet, 'patient')
router.register(r'exam', ExamModelViewSet, 'exam')

app_name = 'patient'
urlpatterns = [
    path('', include(router.urls)),
]
