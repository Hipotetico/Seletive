from django.db import models

# Create your models here.

class Tecnologias(models.Model):
    tecnologia = models.CharField(max_length=30)

    def __str__(self):
        return self.tecnologia

class Empresa(models.Model):

    choices_nicho_mercado = (
        ('M', 'Mercado'),
        ('N', 'Nutrição'),
        ('D', 'Design')
    )

    logo = models.ImageField(upload_to='logo_empresa')
    nome = models.CharField(max_length=30)
    email = models.EmailField()
    cidade = models.CharField(max_length=30)
    endereco = models.CharField(max_length=30)
    caracteristica_empresa = models.TextField()
    nicho_mercado = models.CharField(max_length=3, choices=choices_nicho_mercado)
    tecnologia = models.ManyToManyField(Tecnologias)

    def __str__(self):
        return self.nome
    
    def qtd_vagas(self):
        return Vagas.objects.filter(empresa__id=self.id).count()
    

class Vagas(models.Model):
    choices_experiencia = (
        ('J', 'Junior'),
        ('P', 'Pleno'),
        ('S', 'Senior')
    )

    choices_status = (
        ('I', 'Interesse'),
        ('C', 'Curriculo Enviado'),
        ('E', 'Entrevista'),
        ('D', 'Desafio Técnico'),
        ('F', 'Finalizado')
    )

    empresa = models.ForeignKey(Empresa, on_delete= models.DO_NOTHING)
    titulo = models.CharField(max_length=30)
    email = models.EmailField(null=True)
    nivel_experiencia = models.CharField(max_length=2, choices=choices_experiencia)
    data_final = models.DateField()
    status = models.CharField(max_length=30, choices=choices_status)
    tecnologias_dominadas = models.ManyToManyField(Tecnologias)
    tecnologias_estudar = models.ManyToManyField(Tecnologias, related_name='Estudar')

    def progresso(self):
        x = [((i+1)*(100/(len(self.choices_status))),j[0]) for i, j in enumerate(self.choices_status)]
        x = list(filter(lambda x: x[1] == self.status, x))[0][0]
        return x

    def __str__(self):
        return self.titulo
    