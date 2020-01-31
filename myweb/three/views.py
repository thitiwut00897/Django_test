from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def student(response):
    return HttpResponse('show all student!!!')

def student_add(response, stadd):
    return HttpResponse('Add student %d person.' %stadd)

def student_edit(response, stedit):
    return HttpResponse('edit student %d person.' %stedit)

def sub(response):
    return HttpResponse('show all subject!!!')

def sub_add(response, subadd):
    return HttpResponse('Add subject %d person.' %subadd)

def sub_edit(response, subedit):
    return HttpResponse('Add subject %d person.' %subedit)
