// Sistema EcoGuardians - JavaScript Interativo
class EcoGuardiansSystem {
    constructor() {
        this.agents = {
            ceo: { name: 'CEO Barbosa Nexus', active: false, tasks: [] },
            development: { name: 'Agente de Desenvolvimento', active: false, tasks: [] },
            design: { name: 'Agente de Design Visual', active: false, tasks: [] },
            analysis: { name: 'Agente de Análise de Dados', active: false, tasks: [] }
        };
        
        this.init();
    }

    init() {
        this.bindEvents();
        this.startSystemAnimations();
        this.addMessage('SISTEMA', 'EcoGuardians iniciado com sucesso.', 'system');
    }

    bindEvents() {
        // Botões de ativação dos agentes
        document.getElementById('activate-ceo').addEventListener('click', () => this.activateAgent('ceo'));
        document.getElementById('activate-dev').addEventListener('click', () => this.activateAgent('development'));
        document.getElementById('activate-design').addEventListener('click', () => this.activateAgent('design'));
        document.getElementById('activate-analysis').addEventListener('click', () => this.activateAgent('analysis'));

        // Console de comandos
        document.getElementById('send-command').addEventListener('click', () => this.sendCommand());
        document.getElementById('command-input').addEventListener('keypress', (e) => {
            if (e.key === 'Enter') this.sendCommand();
        });

        // Limpar console
        document.getElementById('clear-console').addEventListener('click', () => this.clearConsole());
    }

    activateAgent(agentType) {
        const agent = this.agents[agentType];
        
        if (!agent.active) {
            agent.active = true;
            this.updateAgentStatus(agentType, true);
            this.addMessage(agent.name.toUpperCase(), `${agent.name} ativado e pronto para receber comandos.`, 'agent');
            this.addTask(`${agent.name} ativado`, 'completed');
            
            // Simular apresentação do agente
            setTimeout(() => {
                this.agentIntroduction(agentType);
            }, 1000);
            
            // CEO Nexus delega tarefas automaticamente quando ativado
            if (agentType === 'ceo') {
                setTimeout(() => {
                    this.delegateTasks();
                }, 2000);
            }
        } else {
            this.addMessage(agent.name.toUpperCase(), `${agent.name} já está ativo.`, 'agent');
        }
    }

    agentIntroduction(agentType) {
        const introductions = {
            ceo: "Olá! Sou o CEO Barbosa Nexus, maestro do Ecossistema EcoGuardians. Estou aqui para orquestrar e gerenciar todas as operações dos agentes subordinados.",
            development: "Agente de Desenvolvimento online! Especializado em criação de código, módulos de autenticação e desenvolvimento de sistemas.",
            design: "Agente de Design Visual ativo! Pronto para criar interfaces, ícones e elementos visuais para o sistema.",
            analysis: "Agente de Análise de Dados operacional! Especializado em processamento e interpretação de dados de engajamento."
        };

        const agent = this.agents[agentType];
        this.addMessage(agent.name.toUpperCase(), introductions[agentType], 'agent');
    }

    delegateTasks() {
        if (this.agents.ceo.active) {
            this.addMessage('CEO NEXUS', 'Iniciando delegação de tarefas aos agentes subordinados...', 'ceo');
            
            const tasks = [
                { agent: 'development', task: 'Desenvolver módulo de autenticação' },
                { agent: 'design', task: 'Criar ícones para o painel de controle' },
                { agent: 'analysis', task: 'Analisar dados de engajamento de usuários' }
            ];

            tasks.forEach((taskInfo, index) => {
                setTimeout(() => {
                    if (this.agents[taskInfo.agent].active) {
                        this.addMessage('CEO NEXUS', `Delegando '${taskInfo.task}' para ${this.agents[taskInfo.agent].name}.`, 'ceo');
                        this.agents[taskInfo.agent].tasks.push(taskInfo.task);
                        this.addTask(taskInfo.task, 'pending');
                        
                        // Simular execução da tarefa
                        setTimeout(() => {
                            this.executeTask(taskInfo.agent, taskInfo.task);
                        }, 3000 + (index * 1000));
                    }
                }, 1000 + (index * 500));
            });
        }
    }

    executeTask(agentType, task) {
        const agent = this.agents[agentType];
        this.addMessage(agent.name.toUpperCase(), `Executando tarefa: ${task}`, 'agent');
        
        // Simular tempo de execução
        setTimeout(() => {
            this.addMessage(agent.name.toUpperCase(), `Tarefa '${task}' concluída com sucesso!`, 'agent');
            this.updateTaskStatus(task, 'completed');
            
            // Enviar relatório para CEO
            setTimeout(() => {
                this.addMessage(agent.name.toUpperCase(), `Relatório enviado ao CEO Nexus: ${task} finalizada.`, 'agent');
            }, 500);
        }, 2000 + Math.random() * 3000);
    }

    sendCommand() {
        const input = document.getElementById('command-input');
        const command = input.value.trim();
        
        if (command) {
            this.addMessage('USUÁRIO', command, 'user');
            this.processCommand(command);
            input.value = '';
        }
    }

    processCommand(command) {
        const lowerCommand = command.toLowerCase();
        
        if (lowerCommand.includes('status')) {
            this.showSystemStatus();
        } else if (lowerCommand.includes('ativar') || lowerCommand.includes('activate')) {
            if (lowerCommand.includes('ceo') || lowerCommand.includes('nexus')) {
                this.activateAgent('ceo');
            } else if (lowerCommand.includes('desenvolvimento') || lowerCommand.includes('dev')) {
                this.activateAgent('development');
            } else if (lowerCommand.includes('design')) {
                this.activateAgent('design');
            } else if (lowerCommand.includes('análise') || lowerCommand.includes('analise')) {
                this.activateAgent('analysis');
            } else {
                this.addMessage('SISTEMA', 'Especifique qual agente deseja ativar: CEO, Desenvolvimento, Design ou Análise.', 'system');
            }
        } else if (lowerCommand.includes('tarefa') || lowerCommand.includes('task')) {
            this.showActiveTasks();
        } else if (lowerCommand.includes('help') || lowerCommand.includes('ajuda')) {
            this.showHelp();
        } else {
            this.addMessage('SISTEMA', 'Comando não reconhecido. Digite "ajuda" para ver os comandos disponíveis.', 'system');
        }
    }

    showSystemStatus() {
        this.addMessage('SISTEMA', 'Status do Sistema EcoGuardians:', 'system');
        Object.entries(this.agents).forEach(([key, agent]) => {
            const status = agent.active ? 'ATIVO' : 'INATIVO';
            const tasksCount = agent.tasks.length;
            this.addMessage('SISTEMA', `${agent.name}: ${status} (${tasksCount} tarefas)`, 'system');
        });
    }

    showActiveTasks() {
        const allTasks = Object.values(this.agents).flatMap(agent => agent.tasks);
        if (allTasks.length > 0) {
            this.addMessage('SISTEMA', 'Tarefas ativas no sistema:', 'system');
            allTasks.forEach(task => {
                this.addMessage('SISTEMA', `- ${task}`, 'system');
            });
        } else {
            this.addMessage('SISTEMA', 'Nenhuma tarefa ativa no momento.', 'system');
        }
    }

    showHelp() {
        const helpCommands = [
            'Comandos disponíveis:',
            '• status - Mostra o status de todos os agentes',
            '• ativar [agente] - Ativa um agente específico',
            '• tarefa - Lista todas as tarefas ativas',
            '• ajuda - Mostra esta lista de comandos'
        ];
        
        helpCommands.forEach(cmd => {
            this.addMessage('SISTEMA', cmd, 'system');
        });
    }

    addMessage(sender, text, type = 'system') {
        const console = document.getElementById('console-content');
        const timestamp = new Date().toLocaleTimeString();
        
        const messageDiv = document.createElement('div');
        messageDiv.className = `message ${type}`;
        messageDiv.innerHTML = `
            <span class="timestamp">[${timestamp}]</span>
            <span class="sender ${type}">${sender}</span>
            <span class="text">${text}</span>
        `;
        
        console.appendChild(messageDiv);
        console.scrollTop = console.scrollHeight;
    }

    addTask(taskText, status = 'pending') {
        const taskList = document.getElementById('task-list');
        
        const taskDiv = document.createElement('div');
        taskDiv.className = 'task-item';
        taskDiv.innerHTML = `
            <span class="task-text">${taskText}</span>
            <span class="task-status ${status}">${this.getStatusSymbol(status)}</span>
        `;
        
        taskList.appendChild(taskDiv);
    }

    updateTaskStatus(taskText, newStatus) {
        const taskItems = document.querySelectorAll('.task-item');
        taskItems.forEach(item => {
            const textElement = item.querySelector('.task-text');
            if (textElement.textContent.includes(taskText)) {
                const statusElement = item.querySelector('.task-status');
                statusElement.className = `task-status ${newStatus}`;
                statusElement.textContent = this.getStatusSymbol(newStatus);
            }
        });
    }

    getStatusSymbol(status) {
        const symbols = {
            pending: '⏳',
            completed: '✓',
            error: '✗'
        };
        return symbols[status] || '?';
    }

    updateAgentStatus(agentType, active) {
        // Atualizar indicadores visuais se necessário
        const statusIndicators = document.querySelectorAll('.status-indicator');
        // Esta função pode ser expandida para atualizar indicadores específicos
    }

    clearConsole() {
        const console = document.getElementById('console-content');
        console.innerHTML = '';
        this.addMessage('SISTEMA', 'Console limpo.', 'system');
    }

    startSystemAnimations() {
        // Adicionar efeitos visuais extras
        this.animateCircuitLines();
        this.animateDataPoints();
    }

    animateCircuitLines() {
        const lines = document.querySelectorAll('.line');
        lines.forEach((line, index) => {
            setInterval(() => {
                line.style.opacity = Math.random() > 0.5 ? '1' : '0.3';
            }, 1000 + (index * 200));
        });
    }

    animateDataPoints() {
        const points = document.querySelectorAll('.data-point');
        points.forEach((point, index) => {
            setInterval(() => {
                const randomColor = ['#00ffff', '#66ccff', '#0099cc'][Math.floor(Math.random() * 3)];
                point.style.background = randomColor;
                point.style.boxShadow = `0 0 10px ${randomColor}`;
            }, 2000 + (index * 500));
        });
    }
}

// Inicializar o sistema quando a página carregar
document.addEventListener('DOMContentLoaded', () => {
    window.ecoGuardians = new EcoGuardiansSystem();
});

// Adicionar efeitos de hover nos botões
document.addEventListener('DOMContentLoaded', () => {
    const buttons = document.querySelectorAll('.control-btn');
    buttons.forEach(button => {
        button.addEventListener('mouseenter', () => {
            button.style.transform = 'translateY(-2px) scale(1.05)';
        });
        
        button.addEventListener('mouseleave', () => {
            button.style.transform = 'translateY(0) scale(1)';
        });
    });
});

// Efeito de digitação para mensagens importantes
function typeWriter(element, text, speed = 50) {
    let i = 0;
    element.innerHTML = '';
    
    function type() {
        if (i < text.length) {
            element.innerHTML += text.charAt(i);
            i++;
            setTimeout(type, speed);
        }
    }
    
    type();
}

