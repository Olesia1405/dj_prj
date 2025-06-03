from rest_framework import viewsets, generics, filters
from rest_framework.decorators import action
from django.db.models import Avg
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from .models import University, Course, UniversityCourse
from .serializers import UniversitySerializer, CourseSerializer, UniversityCourseSerializer



class UniversityViewSet(viewsets.ModelViewSet):
    queryset = University.objects.all()
    serializer_class = UniversitySerializer
    search_fields = ['name']

    @action(detail=True, methods=['get'])
    def course_stats(self, request, pk=None):
        university = self.get_object()
        courses = UniversityCourse.objects.filter(university=university)

        total_courses = courses.count()
        average_duration = courses.aggregate(avg_duration=Avg('duration_weeks'))['avg_duration']

        stats = {
            'total-courses': total_courses,
            'average_duration': average_duration
        }

        return Response(stats)

class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    search_fields = ['title']



class UniversityCourseViewSet(viewsets.ModelViewSet):
    queryset = UniversityCourse.objects.order_by('-id')
    serializer_class = UniversityCourseSerializer

    filter_backends = [DjangoFilterBackend]
    filterset_fields = {
        "title": ["exact", "contains"],
        'semester': ['exact', 'contains']
    }
    ordering_fields = ['duration_weeks']



class UniversityCoursesList(generics.ListAPIView):
    serializer_class = UniversityCourseSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['semester']
    ordering_fields = ['duration_weeks']

    def get_queryset(self):
        university_id = self.kwargs['id']
        return UniversityCourse.objects.filter(university_id=university_id)