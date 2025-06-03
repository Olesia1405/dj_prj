from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

# Создаём router для ViewSets
router = DefaultRouter()
router.register(r'universities', views.UniversityViewSet)
router.register(r'courses', views.CourseViewSet)
router.register(r'university-courses', views.UniversityCourseViewSet)

urlpatterns = [
    path('', include(router.urls)),
]