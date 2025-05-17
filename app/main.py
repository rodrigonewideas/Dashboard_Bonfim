from fastapi import FastAPI
import fdb
import os
from dotenv import load_dotenv

# Carregar variáveis do .env
load_dotenv(dotenv_path="../.env")

app = FastAPI()

# Configurações do banco Firebird
host = os.getenv("FIREBIRD_HOST")
database = os.getenv("FIREBIRD_DATABASE")
user = os.getenv("FIREBIRD_USER")
password = os.getenv("FIREBIRD_PASSWORD")
charset = os.getenv("FIREBIRD_CHARSET", "ISO8859_1")

@app.get("/ping")
def ping():
    return {"status": "ok", "hostname": os.uname()[1]}

@app.get("/tabelas")
def contar_tabelas():
    try:
        con = fdb.connect(
            host=host,
            database=database,
            user=user,
            password=password,
            charset=charset
        )
        cur = con.cursor()
        cur.execute("SELECT COUNT(*) FROM RDB$RELATIONS")
        result = cur.fetchone()
        con.close()
        return {"tabelas": result[0]}
    except Exception as e:
        return {"erro": str(e)}
