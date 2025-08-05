from sqlalchemy import create_engine
from dotenv import load_dotenv
import os
from sqlalchemy import text

load_dotenv()  # carrega o .env

url = os.getenv("DATABASE_URL")

try:
    engine = create_engine(url)
    with engine.connect() as conn:
        result = conn.execute(text("SELECT 1"))
        print("✅ Conexão bem-sucedida!")
except Exception as e:
    print("❌ Erro ao conectar no banco:", e)

