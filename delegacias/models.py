from django.db import models
from django.db.models import TextField


class Base(models.Model):
    criacao = models.DateTimeField(auto_created=True)
    atualizacao = models.DateTimeField(auto_now=True)
    ativo = models.BooleanField(default=True)

    class Meta:
        abstract = True


class Delegacia(Base):
    localizacao = models.CharField(max_length=140, default='SOME STRING')
    titulo = models.CharField(max_length=255)
    url = models.URLField(unique=True)


    class Meta:
        verbose_name = 'Delegacia'
        verbose_name_plural = 'Delegacias'



    def __str__(self):
        return self.localizacao


class Regiao(Base):
    cidade = models.CharField(max_length=255)
    cep = models.CharField(max_length=10)


    class Meta:
        verbose_name = "Regiao"
        verbose_name_plural = "Regioes"


    def __str__(self):
        return self.cidade




class Avaliacao(Base):
    delegacia = models.ForeignKey(Delegacia, related_name='avaliacoes', on_delete=models.CASCADE)
    nome = models.CharField(max_length=255)
    email = models.EmailField()
    comentario = models.TextField(blank=True, default='')
    avaliacao = models.DecimalField(max_digits=2, decimal_places=1)


    class Meta:
        verbose_name = "Avaliacao"
        verbose_name_plural = "Avaliacoes"
        unique_together = ['email', 'delegacia']

        def __init__(self):
            self.avaliacao = None
            self.delegacia = None
            self.name = None

        def __str__(self):
            return f'{self.name} avaliou a consulta {self.delegacia} com a nota {self.avaliacao}'



