from django.urls import path, include
from . import views
from .views import EstoqueDeleteView,ImportacoesDeleteView
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
import matplotlib.pyplot as plt


app_name = 'estoque'

urlpatterns = [
    path('login/',views.LoginView.as_view(),name = 'login'),
    path('logout/',views.LogoutRedirectView.as_view(),name = 'logout'),
    path('home/,',views.HomeView.as_view(),name = 'home'),
    
    path('importacoes/',views.ImportacoesListView.as_view(),name = 'importacoes'),
    path('importacoes/detail/<int:pk>/',views.ImportacoesDetail.as_view(),name = 'importacao_detalhe'),
    path('importacoes/deletar/<int:pk>/',ImportacoesDeleteView.as_view(),name = 'importacao_delete'),
    path('importacoes/cadastro',views.ImportacoesCadastroProdutoView.as_view(),name = 'importacao_produto'),
    
    path('estoque/',views.EstoqueListView.as_view(),name = 'estoque'),
    path('estoque/deletar/<int:pk>/',EstoqueDeleteView.as_view(), name ='estoque_delete'),
    path('estoque/detail/<int:pk>/',views.EstoqueDetail.as_view(),name = 'estoque_detalhe'),
    path('estoque/cadastro/',views.EstoqueCadastroProdutoView.as_view(),name = 'estoque_cadastro'),

    path('analises/produtos/',views.AnaliseDeProdutosView,name ='analise_de_produtos'),
    path('analises/produtos/teste',views.analise, name = 'analise_produtos'),

    path('analises/vendas/',views.AnaliseDeVendasView.as_view(),name = 'analise_de_vendas'),
    path('analises/vendedores/',views.AnaliseDeVendedoresView.as_view(),name='analise_de_vendedores'),
    path('analises/financas/',views.AnaliseDeFinancasView.as_view(), name='analise_de_financas')
]

urlpatterns += staticfiles_urlpatterns()