from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def final_grade_cal(request):
    current_grade = None
    desired_grade = None
    weight = None
    grade_needed = None

    if request.method == 'POST':
        current_grade=float(request.POST.get('current_grade', 0))
        desired_grade=float(request.POST.get('desired_grade', 0))
        weight=int(request.POST.get('weight', 0))
        grade_needed = (desired_grade -(1 - weight) * current_grade) / weight
    

    return render(request, 'gradetracker/final.html', {'grade_needed' : grade_needed})