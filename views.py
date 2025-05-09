from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def admission_fee(request):
    return HttpResponse("your fee is pending")

def yearly_fee(request):
    return HttpResponse("30k per year")