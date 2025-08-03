# EcoGuardians - Agente IA Real

Esta é a versão online e real dos agentes EcoGuardians, utilizando a API da OpenAI (GPT-4).

## Como executar

1. Renomeie `.env.example` para `.env` e adicione sua chave da OpenAI:
```
OPENAI_API_KEY=sua_chave_aqui
```

2. Instale as dependências:
```
pip install -r requirements.txt
```

3. Rode o servidor:
```
python app.py
```

## Endpoint disponível

### `POST /api/ia/testar`
Envie uma mensagem para o agente IA e receba uma resposta gerada via OpenAI GPT-4.