from sqlalchemy import create_engine

# Defina a URL do banco de dados (inclua client_encoding se necessário)
POSTGRES_DATABASE_URL = "postgresql://postgres:ocean007@localhost:5432/db_ocean"

# Crie o engine
engine = create_engine(POSTGRES_DATABASE_URL)

# Teste a conexão
try:
    # Conecte-se ao banco de dados
    with engine.connect() as connection:
        # Execute uma simples consulta
        result = connection.execute("SELECT 1")
        print("Conexão bem-sucedida! Resultado da consulta:", result.fetchone())
except Exception as e:
    print("Erro ao conectar ao banco de dados:", e)
