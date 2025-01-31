from sqlalchemy import create_engine, text

# String de conexão com o banco de dados 'postgres'
POSTGRES_DATABASE_URL = "postgresql://postgres:ocean007@localhost:5432/postgres"

# Crie o engine usando SQLAlchemy
engine = create_engine(POSTGRES_DATABASE_URL)

# Teste a conexão
try:
    with engine.connect() as connection:
        result = connection.execute(text("SELECT 1"))
        print("Conexão bem-sucedida! Resultado da consulta:", result.fetchone())
except Exception as e:
    print("Erro ao conectar ao banco de dados:", e)
