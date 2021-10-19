from django.db import models

class TimestampableMixin(models.Model):
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    
    updated_at = models.DateTimeField(
        auto_now = True,
        null=True 
    )

    class Meta:
        abstract = True

class Produtos_importacao(TimestampableMixin):
    nome = models.CharField(
        max_length = 60,
        default = "produto"
    )
    
    quantidade = models.IntegerField(
        default = 0,
        blank = True
    )

    descricao = models.CharField(
        max_length = 60,
        blank = True
    )

    preco = models.DecimalField(
        decimal_places = 3,
        max_digits = 6
    )

    frete = models.DecimalField(
        decimal_places= 3,
        max_digits= 6
    )

    def __str__(self):
        return "%s, %s"%(self.nome, self.descricao)

    class Meta:
        verbose_name_plural = "Produtos_importacao"


class Importacao(models.Model):

    produto_importacao = models.ForeignKey( 
        Produtos_importacao, 
        on_delete = models.PROTECT
    )

class Produtos_loja(TimestampableMixin):

    codigo = models.CharField(
        max_length= 45,
        default = "0ACB"
    )

    nome = models.CharField(
        max_length= 45,
        default = "produto"
    )

    quantidade = models.IntegerField(
        default= 0
    )

    preco = models.DecimalField(
        decimal_places = 3,
        max_digits = 6
    )

    status = models.CharField(
        max_length= 45,
        default = "esperando produto",
    )

    def __str__(self):
        return "%s, %s"%(self.codigo, self.nome)

    class Meta:
        verbose_name_plural = "Produtos_da_Loja"