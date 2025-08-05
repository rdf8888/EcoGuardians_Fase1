from flask import Flask, request, jsonify
from flask_cors import CORS
import json
import datetime
from agente_ia import CEONexus, AgenteTarefaEspecifica, GerenciadorAgentes

app = Flask(__name__)
CORS(app)  # Permitir requisições de qualquer origem

# Inicializar o gerenciador de agentes
gerenciador = GerenciadorAgentes()

# Carregar estado dos agentes ou criar novos
def inicializar_agentes():
    gerenciador.carregar_estado()
    
    if not gerenciador.agentes:
        # Criar agentes se não existirem
        ceo_nexus = CEONexus()
        agente_desenvolvimento = AgenteTarefaEspecifica("Agente de Desenvolvimento", "Desenvolvimento de Código")
        agente_design = AgenteTarefaEspecifica("Agente de Design Visual", "Criação de Interfaces e Gráficos")
        agente_analise = AgenteTarefaEspecifica("Agente de Análise de Dados", "Processamento e Interpretação de Dados")
        
        # Adicionar ao gerenciador
        gerenciador.agentes[ceo_nexus.nome] = ceo_nexus
        gerenciador.agentes[agente_desenvolvimento.nome] = agente_desenvolvimento
        gerenciador.agentes[agente_design.nome] = agente_design
        gerenciador.agentes[agente_analise.nome] = agente_analise
        
        # Configurar subordinados
        ceo_nexus.adicionar_agente(agente_desenvolvimento)
        ceo_nexus.adicionar_agente(agente_design)
        ceo_nexus.adicionar_agente(agente_analise)
        
        gerenciador.salvar_estado()

# Inicializar agentes na inicialização do app
inicializar_agentes()

@app.route('/')
def home():
    return jsonify({
        "message": "EcoGuardians API - Sistema de Agentes IA",
        "version": "1.0.0",
        "status": "online"
    })

@app.route('/api/agents', methods=['GET'])
def get_agents():
    """Retorna informações sobre todos os agentes."""
    agents_info = {}
    for nome, agente in gerenciador.agentes.items():
        agents_info[nome] = {
            "nome": agente.nome,
            "funcao": agente.funcao,
            "tarefas": agente.tarefas,
            "mensagens": agente.mensagens,
            "ativo": hasattr(agente, 'ativo') and agente.ativo if hasattr(agente, 'ativo') else False
        }
    
    return jsonify(agents_info)

@app.route('/api/agents/<agent_name>/activate', methods=['POST'])
def activate_agent(agent_name):
    """Ativa um agente específico."""
    agente = gerenciador.obter_agente(agent_name)
    
    if not agente:
        return jsonify({"error": "Agente não encontrado"}), 404
    
    # Marcar como ativo (adicionar propriedade se não existir)
    agente.ativo = True
    
    # Salvar estado
    gerenciador.salvar_estado()
    
    return jsonify({
        "message": f"Agente {agent_name} ativado com sucesso",
        "agent": {
            "nome": agente.nome,
            "funcao": agente.funcao,
            "ativo": True
        }
    })

@app.route('/api/agents/<agent_name>/tasks', methods=['POST'])
def add_task_to_agent(agent_name):
    """Adiciona uma tarefa a um agente específico."""
    data = request.get_json()
    
    if not data or 'task' not in data:
        return jsonify({"error": "Tarefa não especificada"}), 400
    
    agente = gerenciador.obter_agente(agent_name)
    
    if not agente:
        return jsonify({"error": "Agente não encontrado"}), 404
    
    task = data['task']
    agente.adicionar_tarefa(task)
    
    # Salvar estado
    gerenciador.salvar_estado()
    
    return jsonify({
        "message": f"Tarefa adicionada ao agente {agent_name}",
        "task": task,
        "agent_tasks": agente.tarefas
    })

@app.route('/api/agents/<agent_name>/execute', methods=['POST'])
def execute_agent_tasks(agent_name):
    """Executa as tarefas de um agente."""
    agente = gerenciador.obter_agente(agent_name)
    
    if not agente:
        return jsonify({"error": "Agente não encontrado"}), 404
    
    if not agente.tarefas:
        return jsonify({
            "message": f"Nenhuma tarefa pendente para {agent_name}",
            "tasks_executed": []
        })
    
    # Executar tarefas
    tasks_executed = agente.tarefas.copy()
    agente.executar_tarefa()
    
    # Salvar estado
    gerenciador.salvar_estado()
    
    return jsonify({
        "message": f"Tarefas executadas pelo agente {agent_name}",
        "tasks_executed": tasks_executed,
        "remaining_tasks": agente.tarefas
    })

@app.route('/api/ceo/delegate', methods=['POST'])
def delegate_task():
    """CEO Nexus delega uma tarefa para um agente subordinado."""
    data = request.get_json()
    
    if not data or 'task' not in data or 'target_agent' not in data:
        return jsonify({"error": "Tarefa ou agente alvo não especificado"}), 400
    
    ceo = gerenciador.obter_agente("CEO Barbosa Nexus")
    target_agent = gerenciador.obter_agente(data['target_agent'])
    
    if not ceo:
        return jsonify({"error": "CEO Nexus não encontrado"}), 404
    
    if not target_agent:
        return jsonify({"error": "Agente alvo não encontrado"}), 404
    
    task = data['task']
    ceo.delegar_tarefa(task, target_agent)
    
    # Salvar estado
    gerenciador.salvar_estado()
    
    return jsonify({
        "message": f"CEO Nexus delegou '{task}' para {target_agent.nome}",
        "task": task,
        "target_agent": target_agent.nome,
        "target_agent_tasks": target_agent.tarefas
    })

@app.route('/api/messages', methods=['GET'])
def get_all_messages():
    """Retorna todas as mensagens de todos os agentes."""
    all_messages = []
    
    for nome, agente in gerenciador.agentes.items():
        for msg in agente.mensagens:
            all_messages.append({
                "timestamp": datetime.datetime.now().isoformat(),
                "agent": nome,
                "sender": msg['remetente'],
                "message": msg['mensagem']
            })
    
    # Ordenar por timestamp (mais recentes primeiro)
    all_messages.sort(key=lambda x: x['timestamp'], reverse=True)
    
    return jsonify(all_messages)

@app.route('/api/agents/<agent_name>/messages', methods=['GET'])
def get_agent_messages(agent_name):
    """Retorna as mensagens de um agente específico."""
    agente = gerenciador.obter_agente(agent_name)
    
    if not agente:
        return jsonify({"error": "Agente não encontrado"}), 404
    
    return jsonify({
        "agent": agent_name,
        "messages": agente.mensagens
    })

@app.route('/api/agents/<sender_name>/send-message', methods=['POST'])
def send_message(sender_name):
    """Envia uma mensagem de um agente para outro."""
    data = request.get_json()
    
    if not data or 'recipient' not in data or 'message' not in data:
        return jsonify({"error": "Destinatário ou mensagem não especificado"}), 400
    
    sender = gerenciador.obter_agente(sender_name)
    recipient = gerenciador.obter_agente(data['recipient'])
    
    if not sender:
        return jsonify({"error": "Agente remetente não encontrado"}), 404
    
    if not recipient:
        return jsonify({"error": "Agente destinatário não encontrado"}), 404
    
    message = data['message']
    sender.enviar_mensagem(recipient, message)
    
    # Salvar estado
    gerenciador.salvar_estado()
    
    return jsonify({
        "message": "Mensagem enviada com sucesso",
        "sender": sender_name,
        "recipient": data['recipient'],
        "content": message
    })

@app.route('/api/system/status', methods=['GET'])
def get_system_status():
    """Retorna o status geral do sistema."""
    total_agents = len(gerenciador.agentes)
    active_agents = sum(1 for agente in gerenciador.agentes.values() 
                       if hasattr(agente, 'ativo') and agente.ativo)
    total_tasks = sum(len(agente.tarefas) for agente in gerenciador.agentes.values())
    total_messages = sum(len(agente.mensagens) for agente in gerenciador.agentes.values())
    
    return jsonify({
        "system_status": "online",
        "total_agents": total_agents,
        "active_agents": active_agents,
        "total_pending_tasks": total_tasks,
        "total_messages": total_messages,
        "timestamp": datetime.datetime.now().isoformat()
    })

@app.route('/api/system/reset', methods=['POST'])
def reset_system():
    """Reseta o sistema, limpando todas as tarefas e mensagens."""
    for agente in gerenciador.agentes.values():
        agente.tarefas = []
        agente.mensagens = []
        if hasattr(agente, 'ativo'):
            agente.ativo = False
    
    gerenciador.salvar_estado()
    
    return jsonify({
        "message": "Sistema resetado com sucesso",
        "timestamp": datetime.datetime.now().isoformat()
    })

@app.route('/api/simulate/full-workflow', methods=['POST'])
def simulate_full_workflow():
    """Simula um fluxo completo de trabalho do sistema."""
    ceo = gerenciador.obter_agente("CEO Barbosa Nexus")
    
    if not ceo:
        return jsonify({"error": "CEO Nexus não encontrado"}), 404
    
    # Ativar CEO
    ceo.ativo = True
    
    # Tarefas padrão para delegação
    default_tasks = [
        {"agent": "Agente de Desenvolvimento", "task": "Desenvolver módulo de autenticação"},
        {"agent": "Agente de Design Visual", "task": "Criar ícones para o painel de controle"},
        {"agent": "Agente de Análise de Dados", "task": "Analisar dados de engajamento de usuários"}
    ]
    
    results = []
    
    for task_info in default_tasks:
        target_agent = gerenciador.obter_agente(task_info["agent"])
        if target_agent:
            # Ativar agente
            target_agent.ativo = True
            # Delegar tarefa
            ceo.delegar_tarefa(task_info["task"], target_agent)
            results.append({
                "action": "task_delegated",
                "task": task_info["task"],
                "agent": task_info["agent"]
            })
    
    # Salvar estado
    gerenciador.salvar_estado()
    
    return jsonify({
        "message": "Fluxo completo simulado com sucesso",
        "actions": results,
        "timestamp": datetime.datetime.now().isoformat()
    })

if __name__ == '__main__':
    print("Iniciando EcoGuardians API...")
    print("Acesse http://localhost:5000 para verificar se a API está funcionando")
    app.run(host='0.0.0.0', port=5000, debug=True)

