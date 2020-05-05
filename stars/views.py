from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')


def courses(request):
    return render(request, 'courses.html')


def single(request):
    return render(request, 'course-single.html')
