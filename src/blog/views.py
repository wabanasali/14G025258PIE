from dataclasses import fields
import django
from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from blog.models import Post


# Create your views here.
class PostListView(ListView):
    #specify the model for this view
    model = Post
    #specify the fields to be displayed
    fields = ['title', 'author', 'body', 'publish', 'created', 'updated', 'status', 'slug']
    #specify template
    template_name = 'post_list.html'


class PostCreateView(CreateView):
    #specify the model for this view
    model = Post
    #specify the fields to be displayed
    fields = ['title', 'author', 'body', 'publish', 'created', 'updated', 'status', 'slug']
    #specify template
    template_name = 'post_form.html'

class PostDetailView(DetailView):
    #specify the model for this view
    model = Post
    #specify the fields to be displayed
    fields = ['title', 'author', 'body', 'publish', 'created', 'updated', 'status', 'slug']
    #specify template
    template_name = 'post_detail.html'

class PostUpdateView(UpdateView):
    #specify the model for this view
    model = Post
    #specify the fields to be displayed
    fields = ['title', 'author', 'body', 'publish', 'created', 'updated', 'status', 'slug']
    #specify template
    template_name = 'post_detail.html'

class PostDeleteView(DeleteView):
    #specify the model for this view
    model = Post
    #specify the fields to be displayed
    fields = ['title', 'author', 'body', 'publish', 'created', 'updated', 'status', 'slug']
    #specify template
    template_name = 'post_confirm_delete.html'