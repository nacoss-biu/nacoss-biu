from django.shortcuts import render
# from django.http import HttpResponse
# Create your views here.

def index_all(request):
	return render(request, 'notice/all.html', {})