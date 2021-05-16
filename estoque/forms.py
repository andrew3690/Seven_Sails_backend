from django import forms
from .models import Produtos_importacao,Produtos_loja

class ProdutosImportacaoform(forms.Modelform):
    class Meta:
        model = Produtos_importacao
        fields = "__all__"

class ProdutosEstoqueform(forms.ModelForm):
    class Meta:
        model = Produtos_loja
        fields = "__all__"
