from django.shortcuts import get_object_or_404
from rest_framework import permissions, status, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.views import TokenObtainPairView

from api.models import Doctor, Patient, PatientDoctorMapping
from api.serializers import (
    DoctorSerializer,
    MappingCreateSerializer,
    MappingListSerializer,
    PatientSerializer,
    RegisterSerializer,
)


class RegisterView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response(
            {"id": user.id, "username": user.username, "email": user.email},
            status=status.HTTP_201_CREATED,
        )


class LoginView(TokenObtainPairView):
    permission_classes = [permissions.AllowAny]


class PatientViewSet(viewsets.ModelViewSet):
    serializer_class = PatientSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Patient.objects.filter(created_by=self.request.user).order_by("-id")

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)


class DoctorViewSet(viewsets.ModelViewSet):
    queryset = Doctor.objects.all().order_by("-id")
    serializer_class = DoctorSerializer
    permission_classes = [permissions.IsAuthenticated]


class MappingsView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        mappings = PatientDoctorMapping.objects.select_related("patient", "doctor").all()
        serializer = MappingListSerializer(mappings, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = MappingCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        patient = get_object_or_404(Patient, id=serializer.validated_data["patient"].id)
        if patient.created_by_id != request.user.id:
            return Response(
                {"detail": "You can only assign doctors to your own patients."},
                status=status.HTTP_403_FORBIDDEN,
            )
        mapping = serializer.save()
        return Response(
            MappingListSerializer(mapping).data, status=status.HTTP_201_CREATED
        )


class MappingByPatientOrDeleteView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, item_id: int):
        patient = get_object_or_404(Patient, id=item_id, created_by=request.user)
        mappings = (
            PatientDoctorMapping.objects.select_related("patient", "doctor")
            .filter(patient=patient)
            .all()
        )
        serializer = MappingListSerializer(mappings, many=True)
        return Response(serializer.data)

    def delete(self, request, item_id: int):
        mapping = get_object_or_404(PatientDoctorMapping, id=item_id)
        if mapping.patient.created_by_id != request.user.id:
            return Response(
                {"detail": "You can only modify mappings for your own patients."},
                status=status.HTTP_403_FORBIDDEN,
            )
        mapping.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
