from rest_framework import serializers
from ..models import Subject, Course, Module

# serilize Subject model class
class SubjectSerilizer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = ['id', 'title', 'slug']


# serilize module
class ModuleSerilizer(serializers.ModelSerializer):
    class Meta:
        model = Module
        fields = ['title', 'description', 'order']


# serilize courses
class CourseSerilizer(serializers.ModelSerializer):
    modules = ModuleSerilizer(many=True, read_only=True)

    class Meta:
        model = Course
        fields = ['id', 'subject', 'title', 'slug', 'overview', 
                  'created', 'owner', 'modules']
