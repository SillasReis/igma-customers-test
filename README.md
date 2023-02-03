# IGMA Customer API

## 📖 Introdução

API de clientes construída com Django Rest Framework. O projeto permite cadastrar clientes e buscá-los através do CPF, bem como a listagem paginada de todos os clientes da base.

Uma instância em funcionamento da API pode ser encontrada em: [igma-customer-test.herokuapp.com/customers/](https://igma-customer-test.herokuapp.com/customers/).

## 🌳 Variáveis de ambiente

Antes de iniciar o servidor, crie um arquivo .env na raíz do projeto como exemplificado em [template.env](template.env) com as seguintes variáveis de ambiente:

| NOME | DESCRIÇÃO | DEFAULT |
|------|-----------|---------|
| SECRET_KEY | Secret key do Django. Pode ser gerada [aqui](https://djecrety.ir/) | Não definida |
| DEBUG | Habilita ou desabilita o modo debug do Django | False |
| ALLOWED_HOSTS | Hosts permitidos. Necessário quando aplicação não está no modo debug |  |
| PAGE_SIZE | Itens por página nas listagens | 10 |

## ⚙️ Instalação de dependências

Para instalar as dependências do projeto, é necessário ter a versão +3.10.x do python e também o pip instalado. Eexecute o comando `pip isntall -r requirements.txt`.

## 🚶 Migrations

Quase lá! O último passo antes de iniciar o servidor é executar as migrações. Para isso, use o comando `python manage.py migrate`.

## ⏯️ Iniciar o servidor

Pronto! Agora é só executar o comando `python manage.py runserver` e a API estará disponível em [http://localhost:8000/customers].

## 🗺️ Documentação

A documentação completa das rotas e funcionalidades pode ser encontrada via swagger e redoc nas seguintes urls:

* Remoto
  * [Swagger](https://igma-customer-test.herokuapp.com/swagger)
  * [Redoc](https://igma-customer-test.herokuapp.com/redoc)

* Local
  * [Swagger](http://localhost:8000/swagger)
  * [Redoc](http://localhost:8000/redoc)

## ⚗️ Testes

Para rodar os testes automatizados, execute o comando `python manage.py test`.

## 👽 Principais tecnologias utilizadas

* [Django](https://docs.djangoproject.com/en/4.1/)
* [Django Rest Framework](https://www.django-rest-framework.org/)
* [SQLite](https://sqlite.org/index.html)
* [Faker](https://faker.readthedocs.io/en/master/)
* [Heroku](https://www.heroku.com/)
* [Gunicorn](https://gunicorn.org/)
* [Pylama](https://github.com/klen/pylama)
