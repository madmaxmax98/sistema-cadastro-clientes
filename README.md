# Sistema de Cadastro de Clientes

Este é um sistema simples de cadastro de clientes desenvolvido em Python, utilizando SQLite como banco de dados.

## Funcionalidades

- Adicionar novos clientes
- Listar todos os clientes cadastrados
- Atualizar informações de um cliente existente
- Deletar um cliente

## Como executar

1. Certifique-se de ter Python instalado (versão 3.x).
2. Execute o arquivo `main.py`:

```
python main.py
```

3. Siga as instruções no menu para interagir com o sistema.

## Estrutura do Projeto

- `main.py`: Ponto de entrada principal do programa, contém o menu e lógica de interação.
- `cliente.py`: Define a classe `Cliente` com os atributos básicos.
- `database.py`: Contém as funções para interação com o banco de dados SQLite.
- `README.md`: Este arquivo de documentação.

## Banco de Dados

O sistema utiliza um arquivo `clientes.db` (SQLite) para armazenar os dados dos clientes. A tabela `clientes` é criada automaticamente na primeira execução.

## Requisitos

- Python 3.x
- Biblioteca padrão sqlite3 (incluída no Python)