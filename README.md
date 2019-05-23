## Desafio Técnico
Servidor HTTP que, para cada  requisição GET, retorne um JSON cuja chave extenso seja a versão por  extenso do número inteiro enviado no path

## Setup e Start da aplicação sem instalar dependências
```bash
docker-compose up
```

### Realizar uma solicitação
```bash
curl -X GET http://127.0.0.1:5000/-9999
```

### Swagger UI - Hosted via Docker-compose
```
http://127.0.0.1:5000/swagger/
```
