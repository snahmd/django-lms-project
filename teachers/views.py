from django.shortcuts import render
from django.views.generic.list import ListView
from teachers.models import Teacher

# Create your views here.

class TeacherListView(ListView):
    model = Teacher
    template_name = "teachers.html"
    