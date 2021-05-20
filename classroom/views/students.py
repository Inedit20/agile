from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.db.models import Count
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView
from django import forms
from ..decorators import student_required
from ..models import Student
from ..forms import ProfileUpdateForm
from itertools import chain

    # Create your views here.






class FlyerView(CreateView):
    model = Student
    form_class = ProfileUpdateForm
    template_name = 'flyer.html'


class profile(CreateView):
    model = Student
    form_class = ProfileUpdateForm
    template_name = 'inscription.html'
    

    def form_valid(self, form):
        quiz = form.save(commit=False)
        quiz.save()
        form.save_m2m()
        return redirect('confirmation', quiz.pk)



class StudentListView(ListView):
    template_name = 'confirmation.html'
    def get_queryset(self):
        self.quiz = get_object_or_404(Student, pk=self.kwargs['pk'])
        return Student.objects.filter(pk = self.quiz.pk)




class PotentielleListView(ListView):
    model = Student
    ordering = ('created_at', )
    context_object_name = 'quizzes'
    template_name = 'students.html'

    def get_queryset(self):
        queryset = Student.objects.all()
        return queryset
