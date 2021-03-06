"""socialmedia URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls.conf import include, path
from django.views.generic.base import RedirectView
from social import views





urlpatterns = [
   path('home/',views.HomeView.as_view()),
   path('about/',views.AboutView.as_view()),
   # path('contact/',views.ContactView.as_view()),
   path('',RedirectView.as_view(url='home/')),
path('accounts/', include('registration.backends.default.urls')),
path('profile/edit/<int:pk>',views.MYProfileUpdateView.as_view(success_url = '/social/home')),
    path('mypost/create/', views.MYPostCreate.as_view(success_url="/social/mypost")),
    path('mypost/', views.MYPostListView.as_view()),

path('mypost/<int:pk>/', views.MYPostDetailView.as_view()),
    path('mypost/delete/<int:pk>', views.MYPostDeleteView.as_view(success_url="/social/mypost")),


    path('myprofile', views.MYProfileListView.as_view()),

path('myprofile/<int:pk>/', views.MYProfileDetailView.as_view()),


        path('myprofile/follow/<int:pk>', views.follow),
        path('myprofile/unfollow/<int:pk>', views.unfollow),


  path('mypost/like/<int:pk>/', views.like),
        path('mypost/unlike/<int:pk>/', views.unlike),

       path('contact/',views.contact),




]
