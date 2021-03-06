from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.utils.decorators import method_decorator

from django.contrib.auth.decorators import login_required
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.db.models import Q,Count, Avg
from django.views.generic.edit import UpdateView,CreateView, DeleteView
from django.http.response import HttpResponseRedirect
from social.models import MYProfile,MYPost ,PostComment, PostLike, FollowUser, contactinfo
from django.views.generic import TemplateView
from django.http import HttpResponse
# Create your views here.

def follow(req,pk):
    user = MYProfile.objects.get(pk=pk)
    FollowUser.objects.create(profile=user, followed_by = req.user.myprofile)
    return HttpResponseRedirect(redirect_to ='/social/myprofile')

def unfollow(req,pk):
    user = MYProfile.objects.get(pk=pk)
    FollowUser.objects.filter(profile=user, followed_by = req.user.myprofile).delete()
    return HttpResponseRedirect(redirect_to ='/social/myprofile')



def like(req,pk):
    post = MYPost.objects.get(pk =pk )

    PostLike.objects.create(post=post, liked_by = req.user.myprofile)
    return HttpResponseRedirect(redirect_to ='/social/home')

def unlike(req,pk):
    post = MYPost.objects.get(pk =pk )
    PostLike.objects.filter(post=post, liked_by = req.user.myprofile).delete()
    return HttpResponseRedirect(redirect_to ='/social/home')







@method_decorator(login_required,name="dispatch")
class HomeView(TemplateView):
    template_name = 'social/home.html'
    def get_context_data(self, **kwargs):
        context = TemplateView.get_context_data(self,**kwargs)
        followedList= FollowUser.objects.filter(followed_by=self.request.user.myprofile)
        followedList2= []
        for e in followedList:
            followedList2.append(e.profile)
        for e in followedList2:
            print(e)




        si = self.request.GET.get("si")
        if si == None:
            si = ""

        postList= MYPost.objects.filter(Q(uploaded_by__in= followedList2)).filter(Q(subject__icontains = si) | Q(msg__icontains =si)).order_by("-id")[:10]
        for p1 in postList:
            p1.liked = False
            ob = PostLike.objects.filter(post = p1,liked_by=self.request.user.myprofile)
            if ob:
                p1.liked = True
            obList = PostLike.objects.filter(post = p1)
            p1.likedno = obList.count()
        context["mypost_list"] = postList
        return context;





        



class AboutView(TemplateView):
    template_name = 'social/about.html'


class ContactView(TemplateView):
    template_name = 'social/contact.html'

@method_decorator(login_required,name="dispatch")
class MYProfileUpdateView(UpdateView):
    model = MYProfile
    fields = ["name", "age", "address","status","gender","phone_no","description","pic"]

@method_decorator(login_required,name="dispatch")
class MYPostCreate(CreateView):
    model = MYPost
    fields = ["subject", "msg", "pic"]
    def form_valid(self,form):
        self.object = form.save()
        self.object.uploaded_by = self.request.user.myprofile
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())



@method_decorator(login_required,name="dispatch")
class MYPostListView(ListView):
    model = MYPost
    def get_queryset(self):
        si = self.request.GET.get("si")
        if si == None:
            si = ""
        return MYPost.objects.filter(Q(uploaded_by= self.request.user.myprofile)).filter(Q(subject__icontains = si) | Q(msg__icontains =si)).order_by("id")[:10]

@method_decorator(login_required,name="dispatch")
class MYPostDetailView(DetailView):
    model = MYPost


@method_decorator(login_required,name="dispatch")
class MYPostDeleteView(DeleteView):
    model = MYPost





@method_decorator(login_required,name="dispatch")
class MYProfileListView(ListView):
    model = MYProfile
    def get_queryset(self):
        si = self.request.GET.get("si")
        if si == None:
            si = ""
        profList = MYProfile.objects.filter(Q(name__icontains = si) | Q(gender__icontains =si) |Q(status__icontains =si) |Q(age__icontains =si)).order_by("id")[:10]
        for p1 in profList:
           p1.followed = False
           ob = FollowUser.objects.filter(profile = p1, followed_by=self.request.user.myprofile)
           if ob:
             p1.followed = True
        return  profList





@method_decorator(login_required,name="dispatch")
class MYProfileDetailView(DetailView):
    model = MYProfile

# def contact(request):
#     if request.method == "get":
#         Cname = request.GET.get('Cname','')
#         Cemail = request.GET.get('Cemail','')
#         Cphone_no = request.GET.get('Cphone_no','')
#         Cmessage = request.GET.get('Cmessage','')
#         contact = contactinfo(Cname=Cname, Cemail=Cemail, Cphone_no =Cphone_no ,  Cmessage= Cmessage)
#         contact.save()
#     return HttpResponseRedirect(redirect_to ='/social/contact')
#
#

def contact(request):
     if request.method == "POST":
        Cname = request.POST.get('Cname','')
        Cemail = request.POST.get('Cemail','')
        Cphone_no = request.POST.get('Cphone_no','')
        Cmassage  = request.POST.get('Cmassage','')
        contact = contactinfo(Cname=Cname, Cemail=Cemail, Cphone_no =Cphone_no ,  Cmassage =Cmassage )

        contact.save()

     return render(request, 'social/contact.html')
