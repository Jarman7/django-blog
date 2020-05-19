from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from django.utils import timezone
from django.urls import reverse

from .models import Post, About, Project
from .forms import ContactForm

from snowplow_tracker import Emitter, Tracker

class HomeView(generic.ListView):
    template_name = 'blog/index.html'
    context_object_name = 'post_list'
    e = Emitter("localhost:9090")
    t = Tracker(e)

    def get_queryset(self):
        self.t.track_page_view("localhost:8000/home/", "home")
        return Post.objects.filter(
            created_on__lte=timezone.now()
        ).order_by('-created_on')


class PostDetailView(generic.DetailView):
    model = Post
    template_name = 'blog/detail.html'

    def get_queryset(self):
        return Post.objects.filter(created_on__lte=timezone.now())


class ProjectView(generic.ListView):
    template_name = 'blog/projects.html'
    context_object_name = 'projects_list'

    def get_queryset(self):
        return Project.objects.filter(
            created_on__lte=timezone.now()
        ).order_by('-created_on')


class ProjectDetailView(generic.DetailView):
    model = Project
    template_name = 'blog/project-detail.html'

    def get_queryset(self):
        return Project.objects.filter(created_on__lte=timezone.now())


class AboutView(generic.ListView):
    template_name = 'blog/about.html'
    context_object_name = 'about'

    def get_queryset(self):
        print(About.objects.first())
        return About.objects.first()


class ContactView(generic.edit.FormView):
    template_name = 'blog/contact.html'
    form_class = ContactForm
    success_url = '/home/thanks'

    def form_valid(self, form):
        form.send_email()
        return super().form_valid(form)


def thanks(request):
    return(render(request,template_name='blog/thanks.html'))