from django.shortcuts import render

from .models import Student


def home_page(request):
    return render(request, 'home.html')


def about_page(request):
    return render(request, 'about.html')


def student_page(request):
    student = Student.objects.all()
    context = {
        'student' : student
    }
    return render(request, 'student.html', context)