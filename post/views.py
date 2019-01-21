from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from .forms import PostModelForm
from .forms import New_Post
from .forms import PostCommentForm
from .forms import New_Comment
from django.utils import timezone

#Create your views here

def index(request):
	context = {}
	posts = Post.objects.all()
	context['posts'] = posts
	return render(request, 'index.html', context)


def detail(request, post_id):
	context = {}
	context['post'] = Post.objects.get(id=post_id)
	return render(request, 'detail.html', context)


def create(request):
	context = {}
	form = New_Post(initial={"date_created":timezone.now(), "date_updated":timezone.now()})

	if request.method == 'POST':
		form = PostModelForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponse('Post added')

	return render(request, "create.html", {'form': form})


def update(request, post_id):
	context = {}
	post = Post.objects.get(id=post_id)

	if request.method == 'POST':
		form = PostModelForm(request.POST, instance=post)
		if form.is_valid():
			form.save()
			return HttpResponse('Post updated')

		else:
			context['form'] = form
			return render(request, 'update.html', context)
		
	else:
		context['form'] = PostModelForm(instance=post)
		return render(request, 'update.html', context)


def comment(request):
	context = {}
	form = New_Comment(initial={"date_created":timezone.now(), "date_updated":timezone.now()})

	if request.method == 'POST':
		form = PostCommentForm(request.POST)
		if form.is_valid():
			form.save()
			return render(request, 'index.html', context)

	return render(request, "comment.html", {'form': form})