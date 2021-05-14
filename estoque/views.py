from django.shortcuts import render, redirect, reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView,View,RedirectView,ListView, DetailView
from django.contrib.auth import authenticate, login as django_login, logout as django_logout

class LoginView(TemplateView):
	template_name = 'home/auth/login.html'

	def post(self,request,*agrs,**kwargs):
		username = request.POST.get('username')
		password = request.POST.get('password')

		user = authenticate(username = username,password=password)

		if user:
			django_login(request,user)
			return render(request,'home/home.html')
		else:
			message = 'Credenciais invalidas'
			return render(request,self.template_name,{'message':message})

class LogoutRedirectView(LoginRequiredMixin,RedirectView):
	url = '/login/'

	def get(self, request, *args, **kwargs):
		django_logout(request)
		return super().get(request, *args, **kwargs)

class HomeView(LoginRequiredMixin,TemplateView):
	template_name = 'home/home.html'

class ImportacoesListView(LoginRequiredMixin,TemplateView):
	template_name = 'importacoes/lista_de_importacao.html'

class ImportacoesDetail(LoginRequiredMixin,TemplateView):
	template_name = 'importacoes/detalhes/detalhe.html'

class EstoqueListView(LoginRequiredMixin,TemplateView):
	template_name = 'estoque/lista_de_estoque.html'

class EstoqueDetail(LoginRequiredMixin,TemplateView):
	template_name = 'estoque/detalhe_produto/detalhe_produto.html'
	