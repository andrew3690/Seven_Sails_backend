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

    codigo = models.CharField(
        max_length= 45,
        default = "0ACB"
    )

    nome = models.CharField(
        max_length = 60,
        default = "produto"
    )

    status = models.CharField(
        max_length= 45,
        default = "esperando produto",
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

    nome_exportador = models.CharField(
        max_length= 50,
        default ="Nome:",
        blank= False
    )

    pais = models.CharField(
        max_length= 50,
        default ="País:",
        blank= False
    )

    def __str__(self):
        return "%s, %s"%(self.nome, self.descricao)

    class Meta:
        verbose_name_plural = "Produtos_importacao"

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
        default = "produto em estoque",
    )

    def __str__(self):
        return "%s, %s"%(self.codigo, self.nome)

    class Meta:
        verbose_name_plural = "Produtos_da_Loja"