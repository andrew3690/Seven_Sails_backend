from django.shortcuts import render, reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView,RedirectView,ListView, DetailView
from django.contrib.auth import authenticate, login as django_login, logout as django_logout
from django.views.generic.edit import CreateView, DeleteView, FormView
from .models import Produtos_importacao,Produtos_loja
from .forms import RegisterProdutosImportacaoform, RegisterProdutosEstoqueform
import pandas as pd

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
	
	def DataAnalsys(self,request):
		model = Produtos_importacao.objects,all().values()
		df = pd.DataFrame(model)

		mydict = {
			"df":df.to_html()
		}
		
		return render(request,self.template_name,context=mydict)



class ImportacoesListView(LoginRequiredMixin,ListView):
	template_name = 'importacoes/lista_de_importacao.html'
	model = Produtos_importacao

class ImportacoesDetail(LoginRequiredMixin,DetailView):
	template_name = 'importacoes/detalhes/detalhe.html'
	model = Produtos_importacao

class ImportacoesDeleteView(LoginRequiredMixin,DeleteView):
	template_name = 'importacoes/delete/delete.html'
	model = Produtos_importacao
	
	def get_success_url(self):
		return reverse('estoque:importacoes')

class ImportacoesCadastroProdutoView(LoginRequiredMixin,FormView, CreateView):
	template_name = 'importacoes/cadastro/cadastro_produto.html'
	form_class = RegisterProdutosImportacaoform

	def get_success_url(self):
		return reverse('estoque:importacao_produto')

class EstoqueListView(LoginRequiredMixin,ListView):
	template_name = 'estoque/lista_de_estoque.html'
	model = Produtos_loja

class EstoqueDetail(LoginRequiredMixin,DetailView):
	template_name = 'estoque/detalhe_produto/detalhe_produto.html'
	model = Produtos_loja

class EstoqueDeleteView(LoginRequiredMixin,DeleteView):
	model = Produtos_loja
	template_name = 'estoque/delete/delete.html'
	
	def get_success_url(self):
		return reverse('estoque:estoque')

class EstoqueCadastroProdutoView(LoginRequiredMixin, FormView, CreateView):
	template_name = 'estoque/cadastro/cadastro_produto.html'
	form_class = RegisterProdutosEstoqueform
	def get_success_url(self):
		return reverse('estoque:estoque_cadastro')