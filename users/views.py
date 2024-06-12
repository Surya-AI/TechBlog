from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm
from blog.models import *
from .models import *
from django.views.generic import *


# Create your views here.
# def users(request):
#     return render(request, 'users/users.html', {'title': 'Users'})

def getFromArr(arr, indices, *args, **kwargs):
    x = []
    for i in indices:
        x.append(arr[i])
    return x


@login_required
def profile(request, *args, **kwargs):
    try:
        user = User._default_manager.all()[kwargs['pk'] - 1]
    except:
        user = request.user
    print(user.id)

    allow_empty = True
    queryset = None
    model = Post
    paginate_by = None
    paginate_orphans = 0
    context_object_name = 'posts'
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

    return render(request, 'users/profile.html', {'title': 'Profile', 'profileUser': user, context_object_name: queryset})


def people(request):
    return render(request, 'users/people.html', {'title': 'People', 'users': User._default_manager.all()})


users = {
    'user': User.objects.all()
}


class UserListView(ListView):
    model = User
    template_name = 'users/people.html'
    context_object_name = 'users'


def explore(request):
    return render(request, 'users/explore.html', {'title': 'Explore'})


def login(request):
    return render(request, 'users/login.html', {'title': 'Login'})


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'{username}! Your account has been created.')
            return redirect('Login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'title': 'Register', 'form': form})
