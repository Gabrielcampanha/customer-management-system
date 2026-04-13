# Gerenciamento de Clientes (Flask + MySQL + Docker)

## Sobre o projeto
API RESTful para gerenciamento de clientes com interface web integrada.

## Tecnologias
- Python
- Flask
- MySQL (Docker)
- JavaScript
- HTML/CSS

## Funcionalidades
- Criar cliente
- Listar clientes
- Atualizar cliente
- Deletar cliente
- Buscar por intervalo de ID
- Resetar base de dados
- Importar clientes via Excel
- Exportar clientes para Excel
- Inserção em lote (bulk)

## Interface
Interface web simples consumindo a API via fetch.

## Como rodar

```bash
# criar ambiente virtual
python -m venv .venv

# ativar
.venv\Scripts\activate

# instalar dependências
pip install -r requirements.txt

# rodar API
python app.py