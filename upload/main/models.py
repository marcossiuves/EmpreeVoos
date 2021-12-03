from django.db import models
from stdimage.models import StdImageField
from django.db.models import signals
from django.template.defaultfilters import slugify
from django.urls import reverse

# Create your models here.
class Base(models.Model):

    create_date = models.DateField('Data de Criação', auto_now_add=True)
    modify_date = models.DateField('Data de Atualização', auto_now=True)
    verified_user = models.BooleanField('Verificado', default=True)

    class Meta:
        abstract = True

class Agendamento(Base):

    destino = models.CharField('Destinos:', max_length=200)
    dataInicial = models.CharField('Ida:', max_length=8)
    dataFinal = models.CharField('Volta:', max_length=8)
    contratante = models.CharField('Contratante:', max_length=200)
    valorPgt = models.IntegerField('Total a pagar:')

    class Meta:
        ordering = ('valorPgt',)
        verbose_name = 'agendamento'
        verbose_name_plural = 'agendamentos'

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse(
            'destinos:agendamentos',
            kwargs={
                'id_agendamento':self.id,
                'slug_destinos': self.slug
                }
            )

class Destinos(Base):

    nomeDestino = models.CharField('NomeDestino', max_length=200)
    precoPorPessoa = models.DecimalField('PrecoPorPessoa', max_digits=8, decimal_places=2)
    descricao = models.TextField(blank=True)
    imagem = StdImageField('Imagem', upload_to='img', variations={'thumb': (300, 300)})
    slug = models.SlugField('Slug', max_length=250, unique=True, blank=True, editable=False)

    class Meta:
        ordering = ('nomeDestino',)
        verbose_name = 'destino'
        verbose_name_plural = 'destinos'

    def __str__(self):
        return self.nomeDestino

    def get_absolute_url(self):
        return reverse(
            'destinos:listar_destinos_por_nomeDestino',
            kwargs={
                'slug_destinos': self.slug
                }
            )

def agendamento_pre_save(signal, instance, sender, **kwargs):
    instance.slug = slugify(instance.name)

def destinos_pre_save(signal, instance, sender, **kwargs):
    instance.slug = slugify(instance.nomeDestino)

signals.pre_save.connect(agendamento_pre_save, sender=Agendamento)
signals.pre_save.connect(destinos_pre_save, sender=Destinos)

