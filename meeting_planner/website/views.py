from django.http import HttpResponse
from django.shortcuts import render

from datetime import datetime

def welcome(request):
    return HttpResponse("Welcome to the Meeting planner! This is a default welcome page automatically generated at " + str(datetime.now()))