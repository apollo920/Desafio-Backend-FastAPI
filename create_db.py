from app.database import Base, engine

print("Criando tabelas...")
Base.metadata.drop_all(bind=engine)
# Base.metadata.create_all(bind=engine)
print("Tabelas criadas com sucesso!")