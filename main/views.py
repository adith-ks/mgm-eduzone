from django.shortcuts import render
from .models import Note

def home(request):
    return render(request, 'main/index.html')

def about(request):
    return render(request, 'main/about.html')

def notes(request):
    semester = request.GET.get('semester')

    if semester:
        notes = Note.objects.filter(semester=semester).order_by('module')
    else:
        notes = Note.objects.all().order_by('semester', 'module')

    return render(request, 'main/notes.html', {'notes': notes})

def contact(request):
    return render(request, 'main/contact.html')