4294 001 919
568 4693 221
#7Glmf*8

Django é um framework web Python de alto nível que incentiva o desenvolvimento rápido e um design limpo e pragmático.

Cuida de grande parte da complexidade do desenvolvimento web, para que você possa se concentrar em escrever seu aplicativo sem precisar reinventar a roda.

É gratuito e de código aberto.

---

 levar os aplicativos do conceito à conclusão o mais rápido possível;

 leva a segurança a sério e ajuda os desenvolvedores a evitar muitos erros comuns de segurança;

 sites mais movimentados da web aproveitam a capacidade do Django de escalar de forma rápida e flexível.

---

Criar PROJETO - django



python -m venv .venv

.venv\\Scripts\\activate

---

Instalar a biblioteca

pip install django

---

Cria o projeto - já vem pastas prontas - pasta de config de vários programa diferentes;

Dentro do Projetos - varias aplicações;



\*\* Model view template

---

Criar o projeto

django-admin startproject (nome do projeto)

django-admin startproject projeto\_crud

---

arquivo importante (manage.py) executa

\* settings.py ----->

\* urls.py ----->

---

ARQUIVO -- **\* settings.py**

Um dicionário contendo as configurações para todos os bancos de dados

https://docs.djangoproject.com/en/5.2/ref/settings/#databases

Dicionário:



DATABASES = {

    'default': {

        'ENGINE': 'django.db.backends.sqlite3',

        'NAME': BASE\_DIR / 'db.sqlite3',

    }

}

Alteração:

==> 'NAME': BASE\_DIR / 'db.crud.db',



Se for utilizar o Mysql deve instalar

pip install mysqlclient

---

Entrar no terminal na pasta do projeto

cd projeto_crud

---

Para Rodar o servidor

python manage.py runserver



qdo executar - vai gerar o banco ==> db.crud.db

---

Rodar aplicação Digitar no NAVEGADOR

http://127.0.0.1:8000/

ou

localhost:8000/



==> The install worked successfully! Congratulations!

---

Aparece no terminal:

September 15, 2025 - 20:04:12

Django version 5.2.6, using settings 'projeto\_crud.settings'

Starting development server at http://127.0.0.1:8000/

---

Recursos do django

http://127.0.0.1:8000/admin

Pagina de administração do Projeto

Django administration

login e senha

http://127.0.0.1:8000/admin/login/?next=/admin/

---

fechar o servidor

Comando:  Ctrl + C

---

criar aplicação

python manage.py startapp (nome\_aplicaçao)

python manage.py startapp crud\_app

------Arquivos a utilizar

models.py

views.py

---

Criar o super Usuario - acessar o admin

Fazer o migrations : ---> vai gerar as entidades do banco

alterar

excluir

relacionamento

---

Fazer o migrations - Executar 2 comando :

Comando:

python manage.py makemigrations



Criar as tabelas - padrão

python manage.py migrate



f1 open database

seleciona o projeto db.database

---

python manage.py createsuperuses

username: admin

Email address: admin@admin.com

password:admin

y

---

roda o servidor novamente

python manage.py runserver

navegador

http://127.0.0.1:8000/admin

---

MODULO - DESING PARTHENER - ARQ SISTEMA - PARTES

Varias estruturas -



ARQUITETURAS

MVC -  MODEL VIEW CONTROLE

Model (classes Model)

entidade do banco

View - front end da aplicação () html,css,js

Controler - classe como função movimentar os dados da view para model ou vice e versa

faz na mão as controle



django =:> mvt - Model View template

mvt --- funciona da mesma forma mvc

as controle já vem pronta

o trabalho e fazer a model e view

==============================================

CRIAR ENTIDADE PESSOA

ABRIR O ARQUIVO models.py

as classes ficaram neste arquivo (todas)

----Criar classes

\# Create your models here.

class Pessoa(models.Model):

---

---

---

=======================================

doc settings.py

incluir o nome da aplicação neste arquivo

INSTALLED\_APPS = \[

    'django.contrib.admin',

    'django.contrib.auth',

    'django.contrib.contenttypes',

    'django.contrib.sessions',

    'django.contrib.messages',

    'django.contrib.staticfiles',

    'crud\_app'

]

===========================================

no Terminal -- execute

a classe foi migrada para o bando

==> python manage.py makemigrations

fara uma mudança no models.py

Na tabela sqlite explorer --->será criada um crud\_app\_pessoa


==> python manage.py migrate

--Applying crud\_app.0001\_initial... OK
----------------------------------------------------------------------------------------------------------

aula 16/09/2025
Alteração cod.
RETIRAR OS ATRIBUTOS ALTURA E DATA_NASCIMENTO
ACRESCENTAR O ATRIBUTO CPF
-------------------------------------------------------------------------
# Create your models here.
class Pessoa(models.Model):
    # definir os atributos da classe 
    id_pessoa = models.AutoField(primary_key=True) # AutoFild autoincremente e primaryKey
    nome = models.CharField(max_length=255, null=False, blank=False)
    email = models.EmailField(unique=True, null=False, blank=False)
    cpf = models.CharField(max_length=14, unique=True, null=True, blank=True)

============================================================================

Entra no projeto
cd projeto_crud

SQLite: open database
projeto_crud db.crud.db 
----------------
Prepara para executar -- equiv. a add .
comando usado para criar novas migrações com base nas alterações feitas nos seus modelos.
Traduz essas alterações detectadas no modelo em um conjunto de operações de esquema de banco de dados e as empacota em um novo arquivo Python dentro do migrationsdiretório do seu aplicativo.

==> python manage.py makemigrations   

-----------------------------------
Esse comando e usado para aplicar migrações de banco de dados.
python manage.py migrate         
=====================================================================================
+NOVO
ACESSAR O SQLITE PARA ELIMINAR COM O COMANDO
-- SQLite
TRUNCATE crud_app_pessoa
EXECUTAR RUN QUERY
-----------------
MODELS.PY
-----------

HABILITAR O CRUD - vem pronto no ADMIN
arquivo ===> admin.py

# importar a Models
from .models import Pessoa

# Register your models here.
admin.site.register(Pessoa)


==> python manage.py makemigrations 
==> python manage.py migrate 
=====================================================================================
Roda a aplicação
python manage.py runserver 

http://localhost:8000/admin/

crud_app/pessoa/add/
=====================================================================================
Alteraçao na (métodos especiais) arquivo models.py
   # metodo especial fornecer uma representação string legível uma instância de classe 
    def __str__(self):
        return self.nome

==> python manage.py makemigrations 
==> python manage.py migrate 

http://localhost:8000/admin
=====================================================================================

VIEW.PY

# Create your views here.
def home(request):
    return HttpResponse("Olá, Mundo Django!!!!")
===================================================
dentro CRUD_APP cria um novo arquivo urls.py

from django.urls import path
from. import views


urlpatterns = [
    path('', views.home, name='home')
]
====================================================
urls.py da pasta projeto_crud

Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('crud_app.urls'))
]
=======================================
AULA 17/09/2025
=======================================
Criar dentro da pasta crud_app pasta 
template
arquivo home.html

conteúdo : https://getbootstrap.com/docs/5.3/getting-started/introduction/
o 2º - Include Bootstrap’s CSS and JS.
Hello, world!
=======================

ARQUIVO view.py
# Create your views here.
def home(request):
    return render(request, "home.html")
================================
arquivo urls.py do projeto

urlpatterns = [
    path('admin/', admin.site.urls),
    path('crud_app', include('crud_app.urls'))
]

==> navegador
http://localhost:8000/crud_app
===========================================






                                                                                                                                             