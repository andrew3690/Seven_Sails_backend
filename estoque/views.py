from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView

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

class HomeView(LoginRequiredMixin,TemplateView):
	template_name = 'home/home.html'