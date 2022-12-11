# Teste Shaped

Este serviço é responsável por criar, listar, atualizer e excluir pacientes e exames


### Clone o Repositório:
```shell script
git clone git@github.com:victorfarruda/shaped-test.git
```

### Configurando projeto

#### Dependências

1. [Install docker](https://docs.docker.com/install/)
2. [Install docker-compose](https://docs.docker.com/compose/install/)

Entre na pasta do projeto:
```shell script
cd shaped-test/
```
Agora vamos buildar o projeto:
```shell script
docker build . -t shaped-test_web
ou
docker-compose build
```

Rodar Migrations:
```shell script
docker-compose run web python manage.py migrate 
```

Você pode rodar o projeto:
```shell script
docker-compose up -d web
```

O projeto está rodando em:
```shell script
http://127.0.0.1:8500
```

Os endpoints existentes são:
```shell script
http://127.0.0.1:8500/api/patient/
http://127.0.0.1:8500/api/exam/
```

Body das requisições:
```shell script
patient:
  {
    "name": "Victor de Freitas Arruda",
    "age": 26,
    "address": "Rua dos Xavantes, 491, Santa Mônica, Belo Horizonte"
  }
exam:
  {
    "name_professional": "Victória",
    "date": "2022-11-12",
    "weight": 74,
    "height": 1.77,
    "patient": 1,
  }
```

Para rodar os testes você pode usar o comando:
```shell script
docker-compose up test
```