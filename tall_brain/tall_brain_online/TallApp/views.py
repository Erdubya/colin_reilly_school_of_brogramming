from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Hello, brofessor! Please proceed to fugma.")

def cumbox(request):
    return HttpResponse("This is a bad place, leave immediately. ╰⋃╯╰⋃╯╰⋃╯╰⋃╯╰⋃╯")
