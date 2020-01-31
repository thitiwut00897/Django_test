from django.http import HttpResponse
from urllib import request
from django.shortcuts import render


# Create your views here.
def subject_today(request, tid):
    return HttpResponse('Login to show subject today!! %d .' %tid)

def subject_detail(request, cid):
    return HttpResponse('detail each subject??? %d' %cid)

def showqr(request):
    return HttpResponse('this is QRCODE!!!!')