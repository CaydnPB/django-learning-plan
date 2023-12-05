from django.http import HttpResponse
from django.shortcuts import render
from .models import ProjectBoardIssue

def projectboard(request):
    issues = ProjectBoardIssue.objects.all()
    return render(request, "projectboard/body.html", {'issues': issues})

def titlemethod(request):
    return HttpResponse("<h1>SprintBoard</h1>")