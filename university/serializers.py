from rest_framework import serializers
from .models import University, Course, UniversityCourse

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        read_only_fields = ["id"]
        fields = ['id', 'title', 'description']


class UniversitySerializer(serializers.ModelSerializer):
    class Meta:
        model = University
        read_only_fields = ["id"]
        fields = ['id', 'name', 'country']


class UniversityCourseSerializer(serializers.ModelSerializer):
    university = UniversitySerializer(read_only=True)
    course = CourseSerializer(read_only=True)

    class Meta:
        model = UniversityCourse
        fields = ['id', 'university', 'course', 'semester', 'duration_weeks']