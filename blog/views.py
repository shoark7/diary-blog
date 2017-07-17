from django.conf.urls import url
from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader


def index(request):
    template = loader.get_template('base.html')
    return HttpResponse(template.render())
