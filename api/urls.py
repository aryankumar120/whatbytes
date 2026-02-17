from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api.views import (
    DoctorViewSet,
    LoginView,
    MappingByPatientOrDeleteView,
    MappingsView,
    PatientViewSet,
    RegisterView,
)

router = DefaultRouter()
router.register(r"patients", PatientViewSet, basename="patient")
router.register(r"doctors", DoctorViewSet, basename="doctor")

urlpatterns = [
    path("auth/register/", RegisterView.as_view(), name="register"),
    path("auth/login/", LoginView.as_view(), name="login"),
    path("", include(router.urls)),
    path("mappings/", MappingsView.as_view(), name="mappings"),
    path("mappings/<int:item_id>/", MappingByPatientOrDeleteView.as_view(), name="mappings-item"),
]
