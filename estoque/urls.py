from django.urls import path, include
from . import views

app_name = 'estoque'

urlpatterns = [
    path('login/',views.LoginView.as_view(),name = 'login'),
    path('logout/',views.LogoutRedirectView.as_view(),name = 'logout'),
    path('home/,',views.HomeView.as_view(),name = 'home'),
    path('importacoes/',views.ImportacoesListView.as_view(),name = 'importacoes'),
    path('importacoes/detail/',views.ImportacoesDetail.as_view(),name = 'importacao_detalhe'),
    path('importacoes/create',views.ImportacoesCadastroProdutoView.as_view(),name = 'importacao_produto'),
    path('estoque/',views.EstoqueListView.as_view(),name = 'estoque'),
    path('estoque/detail/',views.EstoqueDetail.as_view(),name = 'estoque_detalhe'),
    path('estoque/cadastro/',views.EstoqueCadastroProdutoView.as_view(),name = 'estoque_cadastro')
]