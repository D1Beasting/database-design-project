from django.shortcuts import render
from django.http import HttpResponse

def home(request):
  return render(request, 'db_project/home.html')
def about(request):
  return render(request, 'db_project/about.html')
