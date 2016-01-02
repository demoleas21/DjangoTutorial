"""View Controller"""

from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    """Site Display"""
    return HttpResponse("Hello, world. You're at the polls index.")

def detail(request, question_id):
    """Question view"""
    return HttpResponse("You're looking at question %s" % question_id)

def results(request, question_id):
    """Result view"""
    response = "You're looking at the result of question %s"
    return HttpResponse(response % question_id)

def vote(request, question_id):
    """Vote view"""
    return HttpResponse("You're voting on question %s" % question_id)
