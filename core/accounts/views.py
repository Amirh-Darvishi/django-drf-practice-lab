from django.shortcuts import render
from django.http import HttpResponse ,JsonResponse
import requests
from .tasks import sendEmail
from time import sleep
from django.views.decorators.cache import cache_page


# Create your views here.


@cache_page(300)
def test(request):
    response = requests.get('https://f02a0381-2920-49e1-8d7e-7862d3b30f41.mock.pstmn.io/test/delay/5')
    return JsonResponse(response.json())



def send_email(request):
    sendEmail.delay()
    return HttpResponse('<h1>Done Sending</h1>')