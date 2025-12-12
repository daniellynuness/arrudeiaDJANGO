# ArrudeiaDJANGO

Projeto Django simples com duas aplicações principais:
- `cadastro` — responsável por funcionalidades de cadastro (usuários/entidades).
- `sistema` — lógica e páginas do sistema.

## Sumário
- Sobre
- Tecnologias
- Pré-requisitos
- Instalação (local)
- Configuração
- Executando a aplicação
- Migrações e banco de dados
- Usuário administrador
- Boas práticas
- Estrutura do projeto
- Contribuindo
- Licença
- Contato

## Sobre
ArrudeiaDJANGO é um projeto baseado em Django com a finalidade de fornecer uma base para cadastro e um sistema web simples. Este README fornece instruções para rodar o projeto localmente e orientações para desenvolvedores que queiram contribuir ou estender a aplicação.

## Tecnologias
- Python (recomenda-se 3.8+)
- Django (versão compatível — use uma versão recente)
- SQLite (banco de dados por padrão, já presente no repositório como `db.sqlite3`)

## Pré-requisitos
- Python instalado (3.8+ recomendado)
- pip
- virtualenv (recomendado)
- Git

## Instalação (local)
1. Clone o repositório:
   git clone https://github.com/daniellynuness/arrudeiaDJANGO.git
   cd arrudeiaDJANGO

2. Crie e ative um ambiente virtual:
   python -m venv .venv
   # Linux / macOS
   source .venv/bin/activate
   # Windows (PowerShell)
   .venv\Scripts\Activate.ps1

3. Instale dependências:
   - Caso contrário, instale Django (versão recomendada):
     pip install "django>=3.2,<5.0"

## Configuração
- Verifique as configurações em `sistema/settings.py` (ou no arquivo equivalente de settings do projeto).
- Segurança:
  - Não deixe a SECRET_KEY exposta em produção. Utilize variáveis de ambiente para configurá-la.
  - Ajuste `DEBUG = False` em produção.
  - Configure `ALLOWED_HOSTS` conforme o domínio/hosts de produção.
- Banco de dados:
  - O repositório já contém `db.sqlite3`. Se preferir começar do zero, remova `db.sqlite3` antes de rodar as migrações.

Exemplo de export de variável de ambiente (Linux/macOS):
export DJANGO_SECRET_KEY='sua-secret-key-aqui'

## Migrações e banco de dados
Aplicar migrações:
python manage.py makemigrations
python manage.py migrate

## Criar usuário administrador
python manage.py createsuperuser

Acesse o admin em:
http://127.0.0.1:8000/admin/

## Executando a aplicação
Para rodar o servidor de desenvolvimento:
python manage.py runserver

Abra no navegador:
http://127.0.0.1:8000/

## Boas práticas
- Não comite credenciais (SECRET_KEY, dados sensíveis, arquivos de configuração com segredos).
- Inclua `db.sqlite3` no `.gitignore` se não quiser versionar o banco de dados local.
- Use um arquivo `.env` ou variáveis de ambiente para configurações sensíveis.

## Estrutura do projeto (visão geral)
- cadastro/ — app responsável por cadastros
- sistema/ — configuração do projeto Django e app principal
- manage.py — utilitário de gerenciamento do Django
- db.sqlite3 — banco de dados SQLite (versão atual do repositório)
