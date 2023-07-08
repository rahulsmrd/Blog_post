from typing import Any
from django.db.models.query import QuerySet
from django.utils import timezone
from django.shortcuts import render,get_object_or_404,redirect
from django.utils import timezone
from django.urls import reverse_lazy,reverse
from blog_app.models import *
from blog_app.forms import *
from django.contrib.auth import login, logout,authenticate
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required #is used for function based views for above in class based views
from django.views.generic import (TemplateView,
                                  ListView,
                                  DetailView,
                                  CreateView,
                                  UpdateView,
                                  DeleteView,)

# Create your views here.

def register(request):
    if request.method =='POST':
        userform=UserForm(request.POST)
        if userform.is_valid():
            user=userform.save()
            user.set_password(user.password)
            user.save()
            return redirect("/")
        
    return render(request,'registration.html', {'form':UserForm})



def login_req(request):
    if request.method =='POST':
        loginform=LoginForm(request.POST)
        username=request.POST.get('username')
        password=request.POST.get('password')

        if loginform.is_valid():
            loginform.save()
            
            user = authenticate(username=username, password=password)
            if user:
                if user.is_active:
                    login(request, user)
                    return redirect(reverse('post_list'))
                
    return render(request, 'login.html', {'form': LoginForm})

@login_required
def logout_req(request):
    logout(request)
    return redirect(reverse("post_list"))


class aboutview(TemplateView):
    template_name="blog_app/about.html"

class postlistview(ListView):
    model=post

    def get_queryset(self) -> QuerySet[Any]:
        return post.objects.order_by('-published_date')

class postdetailview(DetailView):
    model=post

class postcreatview(CreateView,LoginRequiredMixin):
    login_url='/login/'
    redirect_field_name="blog_app/post_detail.html"

    model=post
    form_class=postform

class postupdateview(UpdateView):
    login_url='/login/'
    redirect_field_name="blog_app/post_detail.html"

    model=post
    form_class=postform

class postdeleteview(LoginRequiredMixin,DeleteView):
    model=post
    success_url=reverse_lazy('post_list')

class draftlistview(ListView,LoginRequiredMixin):
    model=post
    login_url='/login/'
    redirect_field_name='blog_app/post_list.html'

    def get_queryset(self) -> QuerySet[Any]:
        return post.objects.filter(published_date__isnull=True).order_by('-creat_date')
    
def add_comment_to_post(request,pk):

    post_comment = get_object_or_404(post,pk=pk)

    if request.method == 'POST':
        form=commentform(request.POST)

        if form.is_valid():
            comment=form.save(commit=False)
            comment.post=post_comment
            comment.save()
            return redirect('post_detail',post_comment.pk)
        
    form=commentform()
    return render(request, 'blog_app/comment_form.html',{'form':form})

@login_required
def comment_approval(request,pk):
    comment_get=get_object_or_404(comment,pk=pk)
    comment_get.approve()
    return redirect('post_detail',comment_get.post.pk)

@login_required
def comment_remove(request,pk):
    comment_get=get_object_or_404(comment,pk=pk)
    post_pk=comment_get.post.pk
    comment_get.delete()
    return redirect('post_detail',post_pk)

@login_required
def post_publish(request,pk):
    Post=get_object_or_404(post, pk=pk)
    Post.publish()
    return redirect('post_detail',pk)