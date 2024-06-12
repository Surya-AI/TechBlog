from django.shortcuts import render
from django.contrib.auth.mixins import *
from django.views.generic import *
from .models import *


# Create your views here.
def home(request):
    blogs = {
        'blog': Blog.objects.all()
    }

    allow_empty = True
    queryset = None
    model = Post
    paginate_by = None
    paginate_orphans = 0
    context_object_name = 'posts'
    # paginator_class = Paginator
    # page_kwarg = "page"
    ordering = ['-date_posted']

    if queryset is not None:
        queryset = queryset
        if isinstance(queryset, QuerySet):
            queryset = queryset.all()
    elif model is not None:
        queryset = model._default_manager.all()
    else:
        raise ImproperlyConfigured(
            "%(cls)s is missing a QuerySet. Define "
            "%(cls)s.model, %(cls)s.queryset, or override "
            "%(cls)s.get_queryset()." % {"cls": self.__class__.__name__}
        )

    if ordering:
        if isinstance(ordering, str):
            ordering = (ordering,)
        queryset = queryset.order_by(*ordering)

    return render(request, 'blog/home.html', { context_object_name: queryset, 'topics': ['Django', 'UkraineConflict', 'TechBlog'] })


class BlogDetailView(DetailView):
    model = Blog
    template_name = 'blog/blogDetail.html'


class BlogCreateView(LoginRequiredMixin, CreateView):
    model = Blog
    template_name = 'blog/blogCreate.html'
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)



class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/postDetail.html'


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'blog/postCreate.html'
    fields = ['content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})

