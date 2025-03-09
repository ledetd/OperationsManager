from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, CreateView, View
from . models import Project, Operation

class Home(TemplateView):
	template_name = 'operations/home.html'

class OperationsList(View):
	def get(self, request):
		operations = Operation.objects.all()
		projects = Project.objects.all()
		return render(request, 'operations/operations_list.html', {'operations': operations, 'projects':projects})