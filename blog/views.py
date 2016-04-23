#coding=utf-8

from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader, Context
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import  BlogPost
from django.db.models import Q
from django.views import generic

import datetime

def blogView(request):

    all_posts = BlogPost.objects.all().order_by('-date')

    paginator = Paginator(all_posts, 6)

    page = request.GET.get('page')

    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    random_posts = BlogPost.objects.order_by('?')[:6]

    templ = loader.get_template('blog.html')

    cont = Context({
        'posts': posts,
        'random_posts': random_posts,
    })

    return HttpResponse(templ.render(cont))

def articleView(request):

    article_id = request.GET.get('article')

    post = BlogPost.objects.get(id=article_id)

    post.read += 1

    post.save()

    random_posts = BlogPost.objects.order_by('?')[:6]

    templ = loader.get_template('article.html')

    cont = Context({
        'post': post,
        'random_posts': random_posts,
    })

    return HttpResponse(templ.render(cont))

def searchView(request):

    keyword = request.GET.get('keyword')


    all_posts = BlogPost.objects.filter(Q(title__icontains=keyword)|Q(content__icontains=keyword)|Q(author__icontains=keyword)).order_by('-date')

    random_posts = BlogPost.objects.order_by('?')[:6]

    templ = loader.get_template('blog.html')

    if all_posts == None:
        cont = Context({
            'random_posts': random_posts,
            'keyword': keyword,
        })

        return HttpResponse(templ.render(cont))

    cont = Context({
        'posts': all_posts,
        'random_posts': random_posts,
        'keyword': keyword,
    })

    return HttpResponse(templ.render(cont))

def friendsView(request):
    templ = loader.get_template('friends.html')
    cont = Context({
    })
    return HttpResponse(templ.render(cont))

