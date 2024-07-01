from django.db import models

# Create your models here.
class Proprietario(models.Model):
    nome = models.CharField(max_length=50)
    telefone = models.CharField(max_length=11)
    def __str__(self):

      return "{} ({})".format(self.nome, self.telefone)

TIPOSEXO = [('M','Macho'), ('F','Femea')]
TIPOANIMAL = [('1', 'Cachorro'), ('2', 'Gato')]

class Animal(models.Model):
    nome = models.CharField(max_length=50)
    especie = models.CharField(choices = TIPOANIMAL, max_length = 10, null = True)
    sexo = models.CharField(choices = TIPOSEXO, max_length = 1, null = True )
    proprietario = models.ForeignKey(Proprietario, on_delete=models.PROTECT)

    def __str__(self):

     return "{} ({}), {}, {}".format(self.nome, self.especie, self.sexo, self.proprietario)

class Veterinario(models.Model):
  nome = models.CharField(max_length = 50)
  crmv = models.CharField(max_length = 5)
  def __str__(self):

      return "{}".format(self.nome)

class ConsultaVeterinaria(models.Model):
  data = models.DateField()
  animal = models.ForeignKey(Animal, on_delete=models.PROTECT)
  descricao = models.CharField(max_length=200,blank=True)
  veterinario = models.ForeignKey(Veterinario,on_delete=models.PROTECT, null=True)

  def __str__(self):
    return "{} motivo: {}. Veterinario: {}".format(self.data,self.descricao,self.veterinario)

  
 