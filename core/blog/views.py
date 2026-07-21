from django.shortcuts import render, redirect
from django.views.generic import (
    TemplateView, RedirectView, ListView, DetailView, FormView, 
    CreateView, UpdateView, DeleteView)

from django.contrib.auth.mixins import (LoginRequiredMixin, 
    PermissionRequiredMixin    )
from blog.models import Post
from blog.forms import *
# Create your views here.

# Function Base View show a template
def indexView(request):
    '''
    a function based view to show index page
    '''
    posts = Post.objects.all()
    context = {'posts':posts}
    return render(request, 'index.html', context)


class IndexView(TemplateView):
    '''
    a class based view to show index page
    '''
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["posts"] = Post.objects.all()
        return context
    



# FBV for redirect
def maktab(request):
    return redirect('https://maktabkhooneh.com')

# CBV for redirect
class Maktab(RedirectView):
    url = 'https://maktabkhooneh.com'




# CBV for list
class PostList(LoginRequiredMixin,PermissionRequiredMixin,ListView):

    context_object_name = 'posts'
    paginate_by = 2
    ordering = '-id'


    queryset = Post.objects.all()
    #model = Post
    # def get_queryset(self):
    #     posts = Post.objects.all()
    #     return posts

    permission_required = 'blog.view_post'


#CBV for detail
class PostDetail(LoginRequiredMixin,DetailView):
    model = Post




# CBV for form
class PostCreate(LoginRequiredMixin,CreateView):
    model = Post
    # fields = ['title', 'content', 'status',
    #           'category', 'published_date']
    form_class = PostForm
    success_url = '/blog/post/'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)




class ContactCreate(FormView):
    template_name = "contact.html"
    form_class = ContactForm
    success_url = "/blog/post/"

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        form.save()
        return super().form_valid(form)
    



class PostUpdate(LoginRequiredMixin,UpdateView):
    model = Post
    form_class = PostForm
    success_url = '/blog/post/'
    template_name_suffix = "_update_form"




class PostDelete(LoginRequiredMixin,DeleteView):
    model = Post
    success_url = '/blog/post/'