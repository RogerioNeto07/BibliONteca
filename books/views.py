from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.mixins import LoginRequiredMixin

from django.views.generic import TemplateView
from django.urls import reverse_lazy

class ViewFeedbackBook(TemplateView):
    login_url = reverse_lazy('user:login')
    template_name = "books/feedback.html"

class ViewDetailBook(TemplateView):
    login_url = reverse_lazy('user:login')
    template_name = "books/detail.html"