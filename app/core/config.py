class Settings:
    api_metadata = {
        "title": "Resume Analyzer",
        "description": "Processa currículos em PDF ou imagem, gerando resumos ou respostas via LLM",
        "version": "1.0.0",
    }
    cors_origins = ["*"]
    mongo_uri = "mongodb://localhost:27017"
    mongo_db = "teste_tecnico_python"

settings = Settings()