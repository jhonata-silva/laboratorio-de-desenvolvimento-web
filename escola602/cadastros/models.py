from django.db import models

# Create your models here.
class Departamento(models.Model):
    nome = models.CharField(max_length=100)
    sigla = models.CharField(max_length=5)

    def __str__(self):
        return "{} ({})".format(self.nome, self.sigla)

class Disciplina(models.Model):
    nome = models.CharField(max_length=100)
    cargaHoraria = models.IntegerField(verbose_name='Carga Horária')
    departamento = models.ForeignKey(Departamento, on_delete=models.PROTECT)

    def __str__(self):
        return "{} - CH: {}".format(self.nome, self.cargaHoraria)

MODALIDADE_CURSO = [
    ('INT', 'Integrado'),
    ('SUB', 'Subsequente'),
    ('CON', 'Concomitante'),
]

class Curso(models.Model):
    nome = models.CharField(max_length=100)
    modalidade = models.CharField(max_length=3, choices=MODALIDADE_CURSO)
    departamento = models.ForeignKey(Departamento, on_delete=models.PROTECT)

    def __str__(self):
        return "{} - {}".format(self.nome, self.modalidade)

TIPO_SALA = [ 
    ('Sala de aula', 'Sala de aula'),
    ('Laboratório', 'Laboratório'),
]

class Sala(models.Model):
    nome = models.CharField(max_length=50)
    tipo = models.CharField(max_length=50, choices=TIPO_SALA)
    
    def __str__(self):
        return "{}".format(self.nome)

DIAS_SEMANA = [
    (0, 'Domingo'),
    (1, 'Segunda-feira'),
    (2, 'Terça-feira'),
    (3, 'Quarta-feira'),
    (4, 'Quinta-feira'),
    (5, 'Sexta-feira'),
    (6, 'Sábado'),
]

TURNO = [('M', 'Matutino'), ('V', 'Vespertino'), ('N', 'Noturno'),]

class Horario(models.Model):
    inicio = models.TimeField(verbose_name='Início')
    fim = models.TimeField()
    turno = models.CharField(max_length=1, choices=TURNO)

    def __str__(self):
        return "{} - {}".format(self.inicio, self.fim)

class HorarioSemana(models.Model):
    descricao = models.CharField(max_length=5)
    dia = models.IntegerField(choices=DIAS_SEMANA)
    horario = models.ForeignKey(Horario, on_delete=models.PROTECT)

    def __str__(self):
        return "{} ({} - {})".format(self.dia, self.horario.inicio, self.horario.fim)
