from django.shortcuts import render
from .models import Blog
from django.http import Http404

def index(request):
	try:
		blog = Blog.objects.all()
		context = {"blogs": blog}
	except Blog.DoesNotExist:
		raise Http404('Page Not Found')
	return render(request, 'bootstrap_test/index.html', context)

def detail(request, slug):
	try:
		BlogDetail = Blog.objects.get(slug=slug)
		context = {"BlogDetail": BlogDetail}
	except Blog.DoesNotExist:
		raise Http404('Page Not Found')
	return render(request, 'bootstrap_test/detail.html', context)

def about(request):
	return render(request, 'bootstrap_test/about.html')
