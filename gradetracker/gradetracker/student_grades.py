from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Grade  # Make sure Grade is correctly imported
from .models import Course
from django.shortcuts import get_object_or_404

# Define the student_grades view
@login_required
def student_grades(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    # Fetch the grades for the logged-in user
    grades = Grade.objects.filter(student=request.user)
    # Rturnr the grades.html template with the fetched grades
    return render(request, 'gradetracker/grades.html', {'grades': grades, 'course': course})
