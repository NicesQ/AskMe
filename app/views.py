from django.http import HttpResponse
from django.core.paginator import Paginator
from django.shortcuts import render
from . import models


def index(request):
    question_list = models.QUESTIONS
    paginator = Paginator(question_list, 20) 
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'index.html', {'page_obj': page_obj})


def question(request, question_id: int):
    if question_id > 99:
        return render(request, '404.html')
    else:
        question_item = models.QUESTIONS[question_id]
        context = {'question': question_item}
        return render(request,'question.html',context=context)
    

def log_in(request):
    return render(request,'log_in.html')


def register(request):
    return render(request,'register.html')


def new_question(request):
    return render(request, 'new_question.html')


def questions_by_tag(request, tag_id: int):
    question_list = models.QUESTIONS
    paginator = Paginator(question_list, 20) 
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'index.html', {'page_obj': page_obj})


def settings(request):
    return render(request, 'settings.html')