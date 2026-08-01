from django.shortcuts import render
from .tasks import sendEmail
from django.http import HttpResponse
from time import sleep


# Create your views here.

def send_email(request):
    sendEmail.delay()
    return HttpResponse('<h1>Done Sending</h1>')
