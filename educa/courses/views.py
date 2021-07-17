from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.edit import (CreateView, 
                                       UpdateView,
                                       DeleteView)
from django.contrib.auth.mixins import (LoginRequiredMixin, 
                                        PermissionRequiredMixin)
from .models import Course


class OwnerMixin(object):
    def get_query(self):
        qs = super().get_queryset()
        return qs.filter(owner=self.request.user)

class OwnerEditMixin(object):
    def form_valid(self, form):
        form.instance.owner = self.request.owner
        return super().form_valid(form)

class OwnerCourseMixin(OwnerMixin,
                       LoginRequiredMixin, 
                       PermissionRequiredMixin):
    model = Course
    fields = ['subject', 'title', 'slug', 'overview']
    success_url = reverse_lazy('manage_course_list')

class OwnerCourseEditMixin(OwnerCourseMixin, OwnerEditMixin):
    template_name = 'manage/course/form.html'

class ManageCourseListView(OwnerCourseMixin, ListView):
    template_name = 'manage/course/list.html'
    permission_required = 'courses.view_course'

class CourseCreateView(OwnerCourseEditMixin, CreateView):
    permission_required = 'courses.add_course'

class CourseUpdateView(OwnerCourseEditMixin, UpdateView):
    permission_required = 'courses.change_course'

class CourseDeleteView(OwnerCourseMixin, DeleteView):
    template_name = 'manage/course/delete.html'
    permission_required = 'courses.delete_course'
