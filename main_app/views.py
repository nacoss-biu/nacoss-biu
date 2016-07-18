from django.shortcuts import render
# from django.http import HttpResponse
from spirit.topic.models import Topic
from models import Exco, Teacher


def index(request):
    context = {
        'show_cover': True,
        'news': Topic.objects.filter(category=3)
    }

    return render(request, 'main_app/index.html', context)


def team(request):
    context = {
        'excos': Exco.objects.order_by('-order'),
        'teachers': Teacher.objects.order_by('-order'),
    }

    return render(request, 'main_app/team.html', context)
