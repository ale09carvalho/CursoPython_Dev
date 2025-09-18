from django.db import models

# Create your models here.
class Pessoa(models.Model):
    # definir os atributos da classe 
    id_pessoa = models.AutoField(primary_key=True) # AutoFild autoincremente e primaryKey
    nome = models.CharField(max_length=255, null=False, blank=False)
    email = models.EmailField(unique=True, null=False, blank=False)
    cpf = models.CharField(max_length=14, unique=True, null=True, blank=True)

    # metodo especial fornecer uma representação string legível uma instância de classe 
    def __str__(self):
        return self.nome
    

