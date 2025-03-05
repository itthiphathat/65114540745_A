from django.views.generic import ListView
from .models import Course

class CourseListView(ListView): 
    model = Course 
    template_name = 'list_courses.html' 
    context_object_name = 'courses'
