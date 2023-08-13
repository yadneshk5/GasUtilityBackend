from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# def say_hello(request):
#     return render(request, 'account_info.html')

def submit_request(request):
    return render(request, 'submit_request.html')

def account_info(request):
    return render(request, 'account_info.html')

def track_request(request):
    return render(request, 'track_request.html')


