# 📊 Dashboard Bonfim

Sistema de análise de contas a receber, desenvolvido em **Python com FastAPI**, utilizando **Firebird 1.5** como banco de dados. O projeto roda em servidor Linux com ambiente virtual isolado, controle de versões via GitHub, e deploy em produção com `systemd`.

---

## 🗂️ Estrutura do Projeto

bonfim/
├── app/ # Código principal da API FastAPI
│ └── main.py # Arquivo de entrada da aplicação
├── alembic/ # Migrações de banco com Alembic
├── bonfim-venv/ # Ambiente virtual Python
├── requirements.txt # Lista de dependências Python
├── .gitignore # Ignora venv, caches, etc.
└── README.md # Este arquivo


---

## ⚙️ Instalações feitas no servidor Linux

```bash
# Atualizações gerais
sudo apt update && sudo apt upgrade -y

# Python 3, pip e venv
sudo apt install python3 python3-pip python3-venv -y

# Firebird Client (caso necessário)
sudo apt install libfbclient2 -y

# Git para controle de versão
sudo apt install git -y

# Criação do ambiente virtual
python3 -m venv bonfim-venv
source bonfim-venv/bin/activate

# Instalação de dependências via pip
pip install fdb alembic fastapi uvicorn python-dotenv

📦 Dependências do requirements.txt
fastapi
uvicorn
fdb
alembic
python-dotenv

🚀 Como executar a API manualmente
# Ativar o ambiente virtual
source bonfim-venv/bin/activate

# Rodar a API com Uvicorn
uvicorn app.main:app --host 0.0.0.0 --port 8000

A API estará disponível em:
http://localhost:8000/docs

🛠️ Execução como serviço (systemd)
Arquivo: /etc/systemd/system/bonfim-api.service

[Unit]
Description=Bonfim API FastAPI Service
After=network.target

[Service]
User=rps
WorkingDirectory=/home/rps/projetos/bonfim
ExecStart=/home/rps/projetos/bonfim/bonfim-venv/bin/uvicorn app.main:app --host 0.0.0.0 --port 8085
Restart=always

[Install]
WantedBy=multi-user.target

Comandos úteis:
sudo systemctl daemon-reexec
sudo systemctl daemon-reload
sudo systemctl enable bonfim-api.service
sudo systemctl start bonfim-api.service
sudo systemctl status bonfim-api.service

🔁 Alembic – Migrações de Banco com Firebird
# Criar nova versão de migração
alembic revision --autogenerate -m "mensagem"

# Aplicar migração ao banco
alembic upgrade head

# Ver versão atual
alembic current

🔐 Git e Backup Automático

    Repositório GitHub:
    https://github.com/rodrigonewideas/Dashboard_Bonfim

    Script automatizado de sincronização:
    /home/rps/git-sync-dashboard-bonfim.sh

    Autenticação via .netrc, armazenado com segurança em /home/rps/.netrc:
machine github.com
login rodrigonewideas
password ghp_SEU_TOKEN_AQUI

🧩 Conexão com banco Firebird
import fdb

conn = fdb.connect(
    dsn='192.168.0.134/3050:C:/solution/data/DIGITALIZADOR.GDB',
    user='SYSDBA',
    password='bonfim2005',
    charset='ISO8859_1'
)

📌 Observações e Extensões Futuras

    Banco de dados Firebird 1.5 rodando em rede

    Projeto hospedado em servidor local (Ubuntu)

    Backend Python + FastAPI já funcional

    Integração futura com frontend em Lovable (Node.js)

    Integração planejada com Supabase como camada de visualização ou painel

    Possibilidade de expandir para containerização com Docker

🧑‍💻 Autor

Rodrigo de Paula Soares
Consultor e desenvolvedor de soluções B2B, automações e análise de dados com Python, Firebird, Linux, Git e infraestrutura local ou híbrida.


---

### ✅ Para aplicar:

1. Crie o arquivo:

```bash
nano /home/rps/projetos/bonfim/README.md


