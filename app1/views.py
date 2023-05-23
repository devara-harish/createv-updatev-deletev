from django.shortcuts import render
from app1.models import *
from django.views.generic import TemplateView,ListView,DetailView,CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy
# Create your views here.

class home(TemplateView):
    template_name='app1/home.html'



class school_List(ListView):
    model=School
    context_object_name='schools'


class School_Detail(DetailView):
    model=School
    context_object_name='sclobject'



class SchoolCreate(CreateView):
    model=School
    fields='__all__'

class SchoolUpdate(UpdateView):
    model=School
    fields='__all__'

class Schooldelete(DeleteView):
    model=School
    context_object_name='schoolobject'
    success_url=reverse_lazy('school_List')

