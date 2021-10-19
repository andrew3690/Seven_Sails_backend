from django.shortcuts import render, redirect, reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView,View,RedirectView,ListView, DetailView
from django.contrib.auth import authenticate, login as django_login, logout as django_logout
from django.views.generic.edit import CreateView, FormView
from .models import Produtos_importacao,Produtos_loja
from .forms import RegisterProdutosImportacaoform, RegisterProdutosEstoqueform

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
	model = Produtos_importacao

class ImportacoesDetail(LoginRequiredMixin,TemplateView):
	template_name = 'importacoes/detalhes/detalhe.html'
	model = Produtos_importacao

class ImportacoesCadastroProdutoView(LoginRequiredMixin,FormView, CreateView):
	template_name = 'importacoes/cadastro/cadastro_produto.html'
	form_class = RegisterProdutosImportacaoform
	def get_success_url(self):
		return reverse('estoque:importacao_produto')

class EstoqueListView(LoginRequiredMixin,TemplateView):
	template_name = 'estoque/lista_de_estoque.html'
	model = Produtos_loja

class EstoqueDetail(LoginRequiredMixin,TemplateView):
	template_name = 'estoque/detalhe_produto/detalhe_produto.html'
	model = Produtos_loja

class EstoqueCadastroProdutoView(LoginRequiredMixin, FormView, CreateView):
	template_name = 'estoque/cadastro/cadastro_produto.html'
	form_class = RegisterProdutosEstoqueform
	def get_success_url(self):
		return reverse('estoque:estoque_cadastro')
	