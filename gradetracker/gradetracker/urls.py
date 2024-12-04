"""
URL configuration for gradetracker project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from django.views.generic import RedirectView
from .student_grades import student_grades
from .student_courses import student_courses
from .final_grade_cal import final_grade_cal



# Login and logout URL
urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='gradetracker/login.html'), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('grades/<int:course_id>', student_grades, name='student_grades'),
    path('', RedirectView.as_view(url='/accounts/login/', permanent=False)), 
    path('accounts/login/home/', student_courses, name='home'),
    path('finalgrade/', final_grade_cal, name='finalgrade'), 
    # password reset 
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='gradetracker/password_reset_form.html'), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='gradetracker/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='gradetracker/password_reset_confirm.html'), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='gradetracker/password_reset_complete.html'), name='password_reset_complete'),
]