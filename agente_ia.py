import abc
import json

class AgenteIA(abc.ABC):
    """Classe abstrata base para todos os agentes de IA no Ecossistema EcoGuardians."""
    def __init__(self, nome: str, funcao: str):
        self.nome = nome
        self.funcao = funcao
        self.tarefas = []
        self.mensagens = []

    @abc.abstractmethod
    def executar_tarefa(self):
        """Método abstrato para a execução de tarefas específicas do agente."""
        pass

    def adicionar_tarefa(self, tarefa: str):
        """Adiciona uma tarefa à lista do agente."""
        self.tarefas.append(tarefa)
        print(f"Tarefa '{tarefa}' adicionada a {self.nome}.")

    def enviar_mensagem(self, destinatario: 'AgenteIA', mensagem: str):
        """Envia uma mensagem para outro agente."""
        print(f"{self.nome} enviando mensagem para {destinatario.nome}: '{mensagem}'")
        destinatario.receber_mensagem(self, mensagem)

    def receber_mensagem(self, remetente: 'AgenteIA', mensagem: str):
        """Recebe uma mensagem de outro agente."""
        self.mensagens.append({'remetente': remetente.nome, 'mensagem': mensagem})
        print(f"{self.nome} recebeu mensagem de {remetente.nome}: '{mensagem}'")

    def _to_dict(self):
        """Converte o objeto do agente em um dicionário para serialização."""
        return {
            'nome': self.nome,
            'funcao': self.funcao,
            'tarefas': self.tarefas,
            'mensagens': self.mensagens
        }

class CEONexus(AgenteIA):
    """Agente Principal (CEO Barbosa Nexus) - Maestro do Ecossistema EcoGuardians."""
    def __init__(self):
        super().__init__("CEO Barbosa Nexus", "Maestro e Gestor Principal")
        self.agentes_subordinados = []

    def adicionar_agente(self, agente: AgenteIA):
        """Adiciona um agente subordinado ao CEO Nexus."""
        self.agentes_subordinados.append(agente)
        print(f"Agente {agente.nome} adicionado como subordinado ao CEO Barbosa Nexus.")

    def delegar_tarefa(self, tarefa: str, agente_alvo: AgenteIA):
        """Delega uma tarefa a um agente específico."""
        print(f"CEO Barbosa Nexus delegando '{tarefa}' para {agente_alvo.nome}.")
        agente_alvo.adicionar_tarefa(tarefa)

    def executar_tarefa(self):
        """Executa as tarefas de alto nível do CEO Nexus."""
        print(f"{self.nome} está executando suas funções de gestão e orquestração.")
        for tarefa in self.tarefas:
            print(f"CEO Nexus processando tarefa: {tarefa}")
        self.tarefas = [] # Limpa as tarefas após execução

class AgenteTarefaEspecifica(AgenteIA):
    """Classe base para agentes especializados em tarefas específicas."""
    def __init__(self, nome: str, funcao: str):
        super().__init__(nome, funcao)

    def executar_tarefa(self):
        """Executa a tarefa específica do agente, processando suas tarefas pendentes."""
        print(f"Agente {self.nome} ({self.funcao}) está executando sua tarefa.")
        if not self.tarefas:
            print(f"Nenhuma tarefa pendente para {self.nome}.")
            return

        for tarefa in self.tarefas:
            print(f"Agente {self.nome} processando tarefa: {tarefa}")
            # Simula a execução da tarefa
            if "autenticação" in tarefa:
                self.enviar_mensagem(ceo_nexus, f"Módulo de autenticação {tarefa} concluído.")
            elif "ícones" in tarefa:
                self.enviar_mensagem(ceo_nexus, f"Criação de ícones {tarefa} finalizada.")
            elif "dados" in tarefa:
                self.enviar_mensagem(ceo_nexus, f"Análise de dados {tarefa} concluída.")
            else:
                self.enviar_mensagem(ceo_nexus, f"Tarefa '{tarefa}' concluída por {self.nome}.")
        self.tarefas = [] # Limpa as tarefas após execução

class GerenciadorAgentes:
    """Gerencia a criação, persistência e recuperação de agentes."""
    def __init__(self, arquivo_estado='agentes_estado.json'):
        self.arquivo_estado = arquivo_estado
        self.agentes = {}

    def carregar_estado(self):
        """Carrega o estado dos agentes de um arquivo JSON."""
        try:
            with open(self.arquivo_estado, 'r') as f:
                estado = json.load(f)
                for agente_data in estado:
                    if agente_data['nome'] == "CEO Barbosa Nexus":
                        agente = CEONexus()
                    else:
                        agente = AgenteTarefaEspecifica(agente_data['nome'], agente_data['funcao'])
                    agente.tarefas = agente_data.get('tarefas', [])
                    agente.mensagens = agente_data.get('mensagens', [])
                    self.agentes[agente.nome] = agente
                # Reconstruir a lista de subordinados para CEO Nexus
                if "CEO Barbosa Nexus" in self.agentes:
                    ceo = self.agentes["CEO Barbosa Nexus"]
                    for nome_subordinado in estado[0].get('agentes_subordinados_nomes', []):
                        if nome_subordinado in self.agentes:
                            ceo.agentes_subordinados.append(self.agentes[nome_subordinado])
            print("Estado dos agentes carregado com sucesso.")
        except FileNotFoundError:
            print("Arquivo de estado não encontrado. Iniciando com agentes vazios.")
        except Exception as e:
            print(f"Erro ao carregar estado dos agentes: {e}")

    def salvar_estado(self):
        """Salva o estado atual dos agentes em um arquivo JSON."""
        estado = []
        for agente in self.agentes.values():
            agente_data = agente._to_dict()
            if isinstance(agente, CEONexus):
                agente_data['agentes_subordinados_nomes'] = [sub.nome for sub in agente.agentes_subordinados]
            estado.append(agente_data)
        with open(self.arquivo_estado, 'w') as f:
            json.dump(estado, f, indent=4)
        print("Estado dos agentes salvo com sucesso.")

    def obter_agente(self, nome: str):
        """Retorna um agente pelo nome."""
        return self.agentes.get(nome)

# Exemplo de uso:
if __name__ == "__main__":
    gerenciador = GerenciadorAgentes()
    gerenciador.carregar_estado()

    if not gerenciador.agentes:
        # Instanciando o CEO Barbosa Nexus
        ceo_nexus = CEONexus()
        gerenciador.agentes[ceo_nexus.nome] = ceo_nexus

        # Instanciando agentes de tarefas específicas
        agente_desenvolvimento = AgenteTarefaEspecifica("Agente de Desenvolvimento", "Desenvolvimento de Código")
        agente_design = AgenteTarefaEspecifica("Agente de Design Visual", "Criação de Interfaces e Gráficos")
        agente_analise = AgenteTarefaEspecifica("Agente de Análise de Dados", "Processamento e Interpretação de Dados")

        gerenciador.agentes[agente_desenvolvimento.nome] = agente_desenvolvimento
        gerenciador.agentes[agente_design.nome] = agente_design
        gerenciador.agentes[agente_analise.nome] = agente_analise

        # Adicionando agentes subordinados ao CEO Nexus
        ceo_nexus.adicionar_agente(agente_desenvolvimento)
        ceo_nexus.adicionar_agente(agente_design)
        ceo_nexus.adicionar_agente(agente_analise)
    else:
        ceo_nexus = gerenciador.obter_agente("CEO Barbosa Nexus")
        agente_desenvolvimento = gerenciador.obter_agente("Agente de Desenvolvimento")
        agente_design = gerenciador.obter_agente("Agente de Design Visual")
        agente_analise = gerenciador.obter_agente("Agente de Análise de Dados")

    # CEO Nexus delegando tarefas
    if ceo_nexus:
        ceo_nexus.delegar_tarefa("Desenvolver módulo de autenticação", agente_desenvolvimento)
        ceo_nexus.delegar_tarefa("Criar ícones para o painel de controle", agente_design)
        ceo_nexus.delegar_tarefa("Analisar dados de engajamento de usuários", agente_analise)

        # CEO Nexus executando sua própria tarefa
        ceo_nexus.executar_tarefa()

    # Agentes executando suas tarefas
    if agente_desenvolvimento: agente_desenvolvimento.executar_tarefa()
    if agente_design: agente_design.executar_tarefa()
    if agente_analise: agente_analise.executar_tarefa()

    # Verificar mensagens recebidas pelo CEO Nexus
    if ceo_nexus and ceo_nexus.mensagens:
        print("\nMensagens recebidas pelo CEO Nexus:")
        for msg in ceo_nexus.mensagens:
            print(f"  De: {msg['remetente']}, Mensagem: {msg['mensagem']}")
        ceo_nexus.mensagens = [] # Limpa as mensagens após leitura

    gerenciador.salvar_estado()


