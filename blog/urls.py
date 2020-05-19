from django.urls import path

from . import views

app_name = 'blog'
urlpatterns = [
    path('', views.HomeView.as_view(), name='index'),
    path('about/', views.AboutView.as_view(), name='about'),
    path('contact/', views.ContactView.as_view(), name='contact'),
    path('thanks/', views.thanks,name='thanks'),
    path('projects/', views.ProjectView.as_view(), name='projects'),
    path('projects/<slug:slug>/', views.ProjectDetailView.as_view(), name='project-detail'),
    path('<slug:slug>/', views.PostDetailView.as_view(), name='detail')
]