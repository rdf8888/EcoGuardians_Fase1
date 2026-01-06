---
title: NEXO V32 Ultra Dialético
emoji: 🔱
colorFrom: black
colorTo: green
sdk: docker
app_port: 7860
---

# 🔱 NEXO V32 | Ultra Dialético

![NEXO](https://img.shields.io/badge/NEXO-Sistema%20de%20IA%20Soberano-00ffff?style=for-the-badge)
![Python](https://img.shields.io/badge/Python-3.11+-blue?style=for-the-badge&logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-0.100+-green?style=for-the-badge&logo=fastapi)
![Groq](https://img.shields.io/badge/Groq-Llama%203.3%2070B-yellow?style=for-the-badge)

## 📋 Descrição

O NEXO V32 é um agente de IA ultra-dialético soberano, projetado para construir soberania digital com lucro 30/30/40 e zero lixo. Utiliza debate interno (Arquiteto vs. Auditor) para decisões estratégicas, com ferramentas externas para execução autônoma.

### 🎯 Características Principais

- **Debate Dialético**: Auto-questionamento com Arquiteto (lucro/rápido) vs. Auditor (crítico/risco)
- **Ferramentas Externas**: Comando seguro, consulta financeira, swarm de sub-agentes, busca web
- **Processamento Multimídia**: Visão para imagens, extração de texto PDF
- **Auto-Evolução**: Geração e instalação de habilidades Python
- **Memória Soberana**: Integração com Supabase para histórico
- **Interface Terminal**: UI futurista estilo terminal hacker

### 🚀 Como Usar

1. **Ordens Diretas**: Digite comandos como "Consulte preço do Bitcoin" ou "Execute ls"
2. **Upload de Arquivos**: Envie PDFs para análise ou imagens para descrição visual
3. **Ferramentas Automáticas**: O AI decide usar ferramentas baseado no debate interno

### 🛠️ Tecnologias

- **IA**: Groq (Llama 3.3 70B, Llama 3.2 Vision)
- **Backend**: FastAPI com Uvicorn
- **Banco**: Supabase (PostgreSQL)
- **Visão**: LangChain para integração multimodal
- **Segurança**: Whitelist de comandos, auto-reparo de dependências

## 🚀 Tecnologias Utilizadas

- **Frontend**: HTML5, CSS3, JavaScript (ES6+)
- **Backend**: Python 3.11+, Flask, Flask-CORS
- **Persistência**: JSON para armazenamento de estado
- **Design**: CSS Grid, Flexbox, Animações CSS, Efeitos Neon

## 📁 Estrutura do Projeto

```
EcoGuardians/
├── index.html              # Interface principal
├── style.css               # Estilos e animações futuristas
├── script.js               # Lógica frontend e interatividade
├── app.py                  # Servidor Flask (API)
├── agente_ia.py            # Sistema de agentes IA
├── requirements.txt        # Dependências Python
├── agentes_estado.json     # Estado persistente dos agentes
└── README.md              # Documentação
```

## 🛠️ Instalação e Configuração

### Pré-requisitos

- Python 3.11 ou superior
- pip (gerenciador de pacotes Python)
- Navegador web moderno

### Passo a Passo

1. **Clone o repositório**
   ```bash
   git clone https://github.com/seu-usuario/ecoguardians.git
   cd ecoguardians
   ```

2. **Instale as dependências**
   ```bash
   pip install -r requirements.txt
   ```

3. **Execute o servidor Flask**
   ```bash
   python app.py
   ```

4. **Abra a interface web**
   - Abra o arquivo `index.html` em seu navegador
   - Ou acesse `http://localhost:5000` se servindo via Flask

## 🎮 Como Usar

### Interface Principal

1. **Ativação do CEO Nexus**
   - Clique no botão "Ativar Maestro" para ativar o agente principal
   - O CEO Nexus automaticamente delegará tarefas aos agentes subordinados

2. **Ativação de Agentes Subordinados**
   - Use os botões "Ativar" para cada agente específico:
     - Agente de Desenvolvimento
     - Agente de Design Visual
     - Agente de Análise de Dados

3. **Console de Comandos**
   - Digite comandos no console para interagir com o sistema
   - Comandos disponíveis:
     - `status` - Mostra o status de todos os agentes
     - `ativar [agente]` - Ativa um agente específico
     - `tarefa` - Lista todas as tarefas ativas
     - `ajuda` - Mostra lista de comandos

### API Endpoints

O sistema oferece uma API RESTful completa:

#### Agentes
- `GET /api/agents` - Lista todos os agentes
- `POST /api/agents/<nome>/activate` - Ativa um agente
- `POST /api/agents/<nome>/tasks` - Adiciona tarefa a um agente
- `POST /api/agents/<nome>/execute` - Executa tarefas de um agente

#### CEO Nexus
- `POST /api/ceo/delegate` - Delega tarefa para agente subordinado

#### Mensagens
- `GET /api/messages` - Lista todas as mensagens
- `GET /api/agents/<nome>/messages` - Mensagens de um agente
- `POST /api/agents/<remetente>/send-message` - Envia mensagem

#### Sistema
- `GET /api/system/status` - Status geral do sistema
- `POST /api/system/reset` - Reseta o sistema
- `POST /api/simulate/full-workflow` - Simula fluxo completo

## 🏗️ Arquitetura do Sistema

### Sistema de Agentes

```python
# Hierarquia dos Agentes
CEO Barbosa Nexus (Maestro)
├── Agente de Desenvolvimento
├── Agente de Design Visual
└── Agente de Análise de Dados
```

### Fluxo de Trabalho

1. **Inicialização**: Sistema carrega estado dos agentes
2. **Ativação**: Usuário ativa CEO Nexus
3. **Delegação**: CEO delega tarefas automaticamente
4. **Execução**: Agentes executam tarefas atribuídas
5. **Comunicação**: Agentes reportam conclusão ao CEO
6. **Persistência**: Estado é salvo automaticamente

## 🎨 Design e Interface

### Elementos Visuais

- **TV Futurista Central**: Holograma rotativo com linhas de circuito
- **Moldura Neon**: Efeitos de brilho pulsante em ciano
- **Painel de Controle**: Botões interativos com hover effects
- **Console**: Terminal estilo sci-fi com mensagens coloridas
- **Animações**: Partículas flutuantes e efeitos de dados

### Responsividade

- Design adaptável para desktop e mobile
- Grid layout flexível
- Elementos redimensionáveis
- Touch-friendly para dispositivos móveis

## 🔧 Personalização

### Modificando Agentes

Para adicionar novos agentes, edite `agente_ia.py`:

```python
# Criar novo agente
novo_agente = AgenteTarefaEspecifica("Nome do Agente", "Função Específica")

# Adicionar ao CEO Nexus
ceo_nexus.adicionar_agente(novo_agente)
```

### Customizando Interface

Modifique `style.css` para alterar:
- Cores do tema (variáveis CSS no topo do arquivo)
- Animações e efeitos
- Layout e dimensões

### Adicionando Funcionalidades

Estenda `script.js` para:
- Novos comandos de console
- Interações adicionais
- Integração com APIs externas

## 🚀 Deploy

### GitHub Pages (Frontend apenas)

1. Faça push do código para GitHub
2. Ative GitHub Pages nas configurações do repositório
3. A interface estará disponível em `https://seu-usuario.github.io/ecoguardians`

### Heroku (Aplicação completa)

1. Crie um `Procfile`:
   ```
   web: python app.py
   ```

2. Configure variáveis de ambiente:
   ```bash
   heroku config:set FLASK_ENV=production
   ```

3. Deploy:
   ```bash
   git push heroku main
   ```

## 🤝 Contribuição

1. Fork o projeto
2. Crie uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

## 📝 Licença

Este projeto está sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.

## 👥 Autores

- **Desenvolvedor Principal** - *Trabalho inicial* - [Seu Nome](https://github.com/seu-usuario)

## 🙏 Agradecimentos

- Inspiração visual baseada em interfaces de ficção científica
- Comunidade open source pelas ferramentas utilizadas
- Contribuidores e testadores do projeto

## 📞 Suporte

Para suporte e dúvidas:
- Abra uma [issue](https://github.com/seu-usuario/ecoguardians/issues)
- Entre em contato via [email](mailto:seu-email@exemplo.com)

---

**EcoGuardians** - Sistema de Agentes IA do Futuro 🚀

