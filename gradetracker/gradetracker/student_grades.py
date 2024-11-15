from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Grade, Assignment  # Make sure Grade is correctly imported
from django.db.models import Sum

# Define the student_grades view
@login_required
def student_grades(request):
    # Fetch the grades for the logged-in user
    grades = Grade.objects.filter(student=request.user)

    courses = {} #list of grades in each course so they can be averaged

    for grade in grades: #loops through a students grades and places them in the appropriate course 
        course = grade.assignment.course
        if course not in courses:
            courses [course] = {
                'total_score' : 0,
                'total_points' : 0
            }

        courses[course]['total_score'] += grade.score 
        courses[course]['total_points']

    course_grades = []

    for course, values in courses.items(): #calculates the total grade for each course
        total_score = values['total_score']
        total_points = values['total_points']
        if total_points > 0: 
            percentage = (total_score / total_points) * 100
        else:
            percentage = 0
        course_grades.append({'course': course, 'total_score':total_score, 'total_points':total_points, 'percentage':percentage})
    

    # Render the grades.html template with the fetched grades
    return render(request, 'gradetracker/grades.html', {'grades': grades, 'course_grades' : course_grades})


#html code for this section that I don't know where to put yet

#<!DOCTYPE html>
#<html lang="en">
#<head>
#    <meta charset="UTF-8">
#    <meta name="viewport" content="width=device-width, initial-scale=1.0">
#    <title>Your Grades</title>
#</head>
#<body>
#    <h1>Your Grades</h1>
#
#    {% if course_grades %}
#        <table border="1">
#            <thead>
#                <tr>
#                    <th>Course</th>
#                    <th>Total Score</th>
#                    <th>Total Points</th>
#                    <th>Percentage</th>
#                </tr>
#            </thead>
#            <tbody>
#                {% for course_grade in course_grades %}
#                    <tr>
#                        <td>{{ course_grade.course.name }} ({{ course_grade.course.code }})</td>
#                        <td>{{ course_grade.total_score }}</td>
#                        <td>{{ course_grade.total_points }}</td>
#                        <td>{{ course_grade.percentage|floatformat:2 }}%</td>
#                    </tr>
#                {% endfor %}
#            </tbody>
#        </table>
#    {% else %}
#        <p>You have no grades yet.</p>
#    {% endif %}
#</body>
#</html>
