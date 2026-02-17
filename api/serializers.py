from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers

from api.models import Doctor, Patient, PatientDoctorMapping

User = get_user_model()


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ("id", "username", "email", "password")

    def validate_password(self, value: str) -> str:
        validate_password(value)
        return value

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data.get("username"),
            email=validated_data.get("email"),
            password=validated_data.get("password"),
        )
        return user


class PatientSerializer(serializers.ModelSerializer):
    created_by = serializers.ReadOnlyField(source="created_by.id")

    class Meta:
        model = Patient
        fields = (
            "id",
            "name",
            "age",
            "gender",
            "address",
            "phone",
            "created_by",
            "created_at",
            "updated_at",
        )


class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = (
            "id",
            "name",
            "specialization",
            "email",
            "phone",
            "created_at",
            "updated_at",
        )


class MappingCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = PatientDoctorMapping
        fields = ("id", "patient", "doctor", "assigned_at")
        read_only_fields = ("id", "assigned_at")


class MappingListSerializer(serializers.ModelSerializer):
    patient = PatientSerializer(read_only=True)
    doctor = DoctorSerializer(read_only=True)

    class Meta:
        model = PatientDoctorMapping
        fields = ("id", "patient", "doctor", "assigned_at")
