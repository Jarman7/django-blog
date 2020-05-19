from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from django.utils import timezone
from django.urls import reverse

from .models import Post, About, Project
from .forms import ContactForm
from .tracking import *
from .CONSTANTS import *



class HomeView(generic.ListView):
    template_name = 'blog/index.html'
    context_object_name = 'post_list'

    t = create_tracker()

    def get_queryset(self):
        url = BLOG_URL + reverse('blog:index')
        self.t.track_page_view(url, "home")

        return Post.objects.filter(
            created_on__lte=timezone.now()
        ).order_by('-created_on')



class PostDetailView(generic.DetailView):
    model = Post
    template_name = 'blog/detail.html'

    t = create_tracker()

    def get_queryset(self):
        posts = Post.objects.filter(created_on__lte=timezone.now())
        post = posts[0]

        url = BLOG_URL + reverse('blog:index') + post.slug
        self.t.track_page_view(url, post.slug)
        
        return posts



class ProjectView(generic.ListView):
    template_name = 'blog/projects.html'
    context_object_name = 'projects_list'

    t = create_tracker()

    def get_queryset(self):
        url = BLOG_URL + reverse('blog:projects')
        self.t.track_page_view(url, "projects")

        return Project.objects.filter(
            created_on__lte=timezone.now()
        ).order_by('-created_on')



class ProjectDetailView(generic.DetailView):
    model = Project
    template_name = 'blog/project-detail.html'

    t = create_tracker()

    def get_queryset(self):
        projects = Project.objects.filter(created_on__lte=timezone.now())
        project = projects[0]

        url = BLOG_URL + reverse('blog:projects') + project.slug
        self.t.track_page_view(url, "Project -" + project.slug)
        
        return projects



class AboutView(generic.ListView):
    template_name = 'blog/about.html'
    context_object_name = 'about'

    t = create_tracker()

    def get_queryset(self):
        url = BLOG_URL + reverse('blog:about')
        self.t.track_page_view(url, "About")

        return About.objects.first()



class ContactView(generic.edit.FormView):
    template_name = 'blog/contact.html'
    form_class = ContactForm
    success_url = '/home/thanks'

    t = create_tracker()

    def get_initial(self):
        url = BLOG_URL + reverse('blog:contact')
        self.t.track_page_view(url, "Contact")
        return super().get_initial()

    def form_valid(self, form):
        form.send_email()
        return super().form_valid(form)



def thanks(request):
    t = create_tracker()
    url = BLOG_URL + reverse('blog:thanks')
    t.track_page_view(url, "Thanks")

    return(render(request,template_name='blog/thanks.html'))