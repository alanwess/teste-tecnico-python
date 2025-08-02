# Resume Analyzer

Essa aplicação permite a analise de múltiplos currículos em PDF ou imagem, gerando resumos automáticos e/ou fazendo perguntas inteligentes sobre o conteúdo dos documentos.

## Como executar

### Requisitos

- Docker
- MongoDB local rodando na porta padrão (27017)

### Build e execução

```bash
docker build -t resume-analyser .
docker run -p 8000:8000 resume-analyser
```

### Acessar Swagger

Abra [http://localhost:8000/docs](http://localhost:8000/docs) para testar a API.

### Exemplo de uso

- Faça upload de PDFs ou imagens.
- Opcionalmente adicione uma `query` para fazer perguntas sobre os currículos.
- O sistema responderá com resumos ou respostas contextualizadas.

## Endpoint de teste

O teste pode ser realizado em http://localhost:8000/v1/analyse via postman com body do tipo multipart/form-data, informando user_id, request_id, query (opcional) e os arquivos desejados.