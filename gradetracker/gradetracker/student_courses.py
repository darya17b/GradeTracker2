from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Course  # Make sure Grade is correctly imported

# Define the student_grades view
@login_required
def student_courses(request):
    # Fetch the courses for the logged-in user
    courses = Course.objects.filter(student=request.user)
    print(courses)
    # Rturnr the grades.html template with the fetched grades
    return render(request, 'gradetracker/home.html', {'courses': courses})
