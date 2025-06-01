from django.contrib import admin
from . import models

@admin.register(models.University)
class UniversityAdmin(admin.ModelAdmin):
    list_display = ['name', 'country']
    search_fields = ['name']

@admin.register(models.Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['title', 'description']
    search_fields = ['title']

@admin.register(models.UniversityCourse)
class UniversityCourseAdmin(admin.ModelAdmin):
    list_display = ['university', 'course', 'semester', 'duration_weeks']
    list_filter = ['semester', 'university']
    search_fields = ['course__title', 'university__name']
