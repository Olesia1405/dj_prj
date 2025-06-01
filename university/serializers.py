from rest_framework import serializers
from .models import University, Course, UniversityCourse

class CourseSerializers(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['id', 'title', 'description']


class UniversitySerializer(serializers.ModelSerializer):
    class Meta:
        model = University
        fields = ['id', 'name', 'country']


class UniversityCourseSerializer(serializers.ModelSerializer):
    university = UniversitySerializer(read_only=True)
    course = CourseSerializers(read_only=True)

    class Meta:
        model = UniversityCourse
        fields = ['id', 'university', 'course', 'semester', 'duration_weeks']