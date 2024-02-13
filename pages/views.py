from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import (TemplateView,
                                  ListView,
                                  DetailView,
                                  CreateView,
                                  UpdateView,
                                  DeleteView,
                                  )

from django.urls import reverse_lazy
from .models import Posts
from .forms import PostForm
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin


class DeletePost(PermissionRequiredMixin, DeleteView):
    permission_required = "pages.delete_post"
    template_name = 'pages/delete_post.html'
    model = Posts
    success_url = reverse_lazy("post_list")
    context_object_name = 'post'


class UpdatePost(PermissionRequiredMixin, UpdateView):
    permission_required = "pages.change_post"
    template_name = 'pages/edit_post.html'
    model = Posts
    form_class = PostForm


class CreateNewPost(LoginRequiredMixin, CreateView):
    template_name = 'pages/post_new.html'
    form_class = PostForm
    model = Posts
    success_url = reverse_lazy('post_list')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


'''Optionally can use create_new_post function instead of CreateNewPost class.
For change view you can go to urls.py in this directory and put the function name instead of class name.
Also notice if you use function you should not use .as_view()'''
# @login_required # use this decorator for apply login permission
# def create_new_post(request):
#     if request.method == 'POST':
#         form = PostForm(request.POST)
#         if form.is_valid():
#             post = form.save(commit=False)
#             post.author = request.user
#             post.save()
#             return redirect('post_list')
#     else:
#         form = PostForm()
#         return render(request, 'pages/post_new.html', context={'form': form})


class PostsDetailView(LoginRequiredMixin, DetailView):
    template_name = 'pages/post_detail.html'
    model = Posts
    context_object_name = 'post'

    def post_detail(request, pk):
        post = get_object_or_404(Posts, pk=pk)
        context = {
            'post': post
        }
        return render(request, 'pages/post_detail.html', context)


'''Optionally can use post_detail function instead of PostDetailView class.
For change view you can go to urls.py in this directory and put the function name instead of class name.
Also notice if you use function you should not use .as_view()'''
# @login_required # use this decorator for apply login permission
# def post_detail(request, pk):
#
#     post = get_object_or_404(Posts, pk=pk)
#     context = {
#         'post': post
#     }
#     return render(request, 'pages/post_detail.html', context)


class PostsListsView(LoginRequiredMixin, ListView):
    template_name = 'pages/Posts.html'
    model = Posts

    def get_queryset(self):
        posts = Posts.objects.filter(is_publish=True)
        return posts


class HomePage(TemplateView):
    template_name = 'pages/index.html'


class AboutPage(TemplateView):
    template_name = 'pages/about.html'


class SearchView(ListView):
    model = Posts
    template_name = 'pages/post_search.html'
    context_object_name = 'all_search_results'

    def get_queryset(self):

        result = super(SearchView, self).get_queryset()
        if query := self.request.GET.get('search'):
            postresult = Posts.objects.filter(Q(title__contains=query) | Q(text__icontains=query))
            result = postresult
        else:
            result = None
        return result
