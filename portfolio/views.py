from django.shortcuts import render, redirect
from portfolio.models import Board, MPTTComment
from django.utils import timezone
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.shortcuts import render
from django.views.generic import ListView, CreateView, DetailView, FormView
from django.contrib.auth import authenticate, login
from django.views import generic
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic.base import TemplateView
from django.contrib.auth.models import User
from portfolio.forms import CreateUserForm, WritePostForm, MPTTCommentForm
from django.db.models import F
from django.views.generic.detail import SingleObjectMixin
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.views.generic.edit import UpdateView
import operator
from django.db.models import Q
from functools import reduce
# Create your views here.
def index(request):
    return render(request, 'index.html')

class BoardListView(ListView):
    model = Board
    template_name = "board.html"
    context_object_name = 'boards'
    paginate_by = 10
    def get_context_data(self, **kwargs):
        context = super(BoardListView, self).get_context_data(**kwargs)
        paginator = context['paginator']
        page_numbers_range = 5
        max_index = len(paginator.page_range)

        page = self.request.GET.get('page')
        current_page = int(page) if page else 1

        start_index = int((current_page - 1) / page_numbers_range) * page_numbers_range
        end_index = start_index + page_numbers_range
        if end_index >= max_index:
            end_index = max_index

        page_range = paginator.page_range[start_index:end_index]
        context['page_range'] = page_range
        return context

class BoardSearchListView(BoardListView):
    def get_queryset(self):
        result = super(BoardSearchListView, self).get_queryset()

        query = self.request.GET.get('q')
        if query:
            query_list = query.split()
            result = result.filter(
                reduce(operator.and_,
                       (Q(title__icontains=q) for q in query_list)) |
                reduce(operator.and_,
                       (Q(memo__icontains=q) for q in query_list))
            )

        return result

class BoardDetail(DetailView, CreateView):
    model = Board
    template_name = 'board-detail.html'
    form_class = MPTTCommentForm
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        Board.objects.filter(pk=self.kwargs['pk']).update(views=F('views')+1)
        return context
    def form_valid(self, form):
        form.instance.board_id = self.kwargs.get('pk')
        return super().form_valid(form)
    def get_success_url(self):
        return reverse('board-detail', kwargs={'pk': self.kwargs['pk']})
    
class CreateUserView(CreateView):
    template_name = 'registration/signup.html'
    form_class =  CreateUserForm
    success_url = reverse_lazy('signup_done')

class RegisteredView(TemplateView):
    template_name = 'registration/signup_done.html'

class WritePostView(CreateView):
    template_name = 'writepost.html'
    form_class = WritePostForm
    success_url = reverse_lazy('board')

@login_required
def comment_remove(request, pk):
    global MPTTComment
    mpttcomment = get_object_or_404(MPTTComment, pk=pk)
    mpttcomment.delete()
    return redirect('board-detail', pk=mpttcomment.board.pk)

@login_required
def board_remove(request, pk):
    boardobject = get_object_or_404(Board, pk=pk)
    boardobject.delete()
    return redirect('board')

class BoardUpdate(UpdateView):
    model = Board
    fields = ['memo']
    template_name = 'board_update_form.html'
    def get_success_url(self):
        return reverse('board-detail', kwargs={'pk': self.kwargs['pk']})

class CommentUpdate(UpdateView):
    model = MPTTComment
    fields = ['comment']
    template_name = 'comment_update_form.html'
    def get_object(self):
        """Returns the BlogPost instance that the view displays"""
        return get_object_or_404(MPTTComment, id=self.kwargs.get("id"))
    def get_success_url(self):
        return reverse('board-detail', kwargs={'pk': self.kwargs['pk']})

