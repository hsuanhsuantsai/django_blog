from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from datetime import datetime
from django.http import HttpResponse
from .models import Post
from django.db.models import Q


def home(request):
	post_list = Post.objects.all()
	return render(request, 'home.html', {'post_list': post_list})

def post_detail(request, pk):
	post = get_object_or_404(Post, pk=pk)
	return render(request, 'post.html', {'post': post})

def tag_list(request, tag):
	post_list = Post.objects.filter(tags__contains=tag)
	if tag == 'Fountain_Pen':
		post_list = Post.objects.filter(tags__contains='fountain').filter(tags__contains='pen')
	elif tag == 'Food_Drinks':
		post_list = Post.objects.filter(Q(tags__contains='food') | Q(tags__contains='drink'))

	return render(request, 'tag_list.html', {'post_list': post_list, 'tag': tag})

def search(request):
	tag = request.POST['keyword']
	print(tag)
	post_list = Post.objects.filter(Q(title__contains=tag) | Q(content__contains=tag) |
					Q(highlight__contains=tag) | Q(location__contains=tag) |Q(tags__contains=tag))
	# return redirect(tag_list, tag=tag)
	return render(request, 'search.html', {'post_list': post_list, 'tag': tag})
