from django.shortcuts import render
from portfolio.models import Board
from django.utils import timezone
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.shortcuts import render
from django.views.generic import ListView, CreateView, DetailView
from django.contrib.auth import authenticate, login
from django.views import generic
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic.base import TemplateView
from django.contrib.auth.models import User
from portfolio.forms import CreateUserForm, WritePostForm

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

class BoardDetail(DetailView):
    model = Board
    template_name = 'board-detail.html'
    query_pk_and_slug = True

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