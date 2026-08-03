from django.shortcuts import render
from django.http import JsonResponse
import requests
# Create your views here.

def test(request):
    response = requests.get('https://f02a0381-2920-49e1-8d7e-7862d3b30f41.mock.pstmn.io/test/delay/5')
    return JsonResponse(response.json())