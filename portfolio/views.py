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
# Create your views here.
def index(request):
    return render(request, 'index.html')


def board(request):
    boardList = Board.objects.all()
    paginator = Paginator(boardList, 10)
    max_index = len(paginator.page_range)

    page = request.GET.get('page')
    boards = paginator.get_page(page)
    page_numbers_range = 5
    current_page = int(page) if page else 1
    start_index = int((current_page - 1) / page_numbers_range) * page_numbers_range
    end_index = start_index + page_numbers_range
    page_range = paginator.page_range[start_index:end_index]
    next_page = start_index + 6
    now = timezone.now
   

    
    if end_index >= max_index:
        end_index = max_index
    context = {
        'boardList': boardList,
        'paginator': paginator,
        'page': page,
        'boards': boards,
        'page_range': page_range,
        'max_index': max_index,
        'current_page': current_page,
        'start_index': start_index,
        'end_index': end_index,
        'page_numbers_range': page_numbers_range,
        'next_page': next_page,
        'now' : now,
        }
    return render(request, 'board.html', context=context)

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
    
""" class Reply(CreateView, DetailView):
    template_name = '_comments.html'
    form_class = ReplyForm
    success_url = reverse_lazy('board')
    def form_valid(self, form):
        form.instance.board_id = self.kwargs.get('pk')
        form.instance.mpttcomment_parent_id = self.kwargs.get('pk')
        return super().form_valid(form)
    def get_success_url(self):
        return reverse('board-detail', kwargs={'pk': self.kwargs['pk']}) """