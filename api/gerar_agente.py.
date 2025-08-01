# api/gerar_agente.py
# Este arquivo consolida toda a lógica de back-end do projeto EcoGuardiões.

import google.generativeai as genai
import os
import json
from abc import ABC, abstractmethod

# ====================================================================
# Configuração de Segurança da API
# ====================================================================
# A chave da API é lida de uma variável de ambiente, garantindo a segurança.
# A chave NUNCA é exposta diretamente no código ou no front-end.
API_KEY = os.environ.get("GEMINI_API_KEY")
model = None

if API_KEY:
    try:
        genai.configure(api_key=API_KEY)
        model = genai.GenerativeModel("gemini-pro")
    except Exception as e:
        print(f"Erro ao configurar a API do Gemini: {e}")

# ====================================================================
# Classes de Agentes (Consolidadas em um só lugar)
# ====================================================================
class AgenteIA(ABC):
    """
    Classe abstrata base para todos os agentes de IA.
    """
    def __init__(self, nome: str, funcao: str):
        self.nome = nome
        self.funcao = funcao
    
    @abstractmethod
    def executar_tarefa(self, descricao_tarefa: str):
        """Método abstrato para a execução de uma tarefa específica."""
        pass

class CEONexus(AgenteIA):
    """
    Agente principal responsável pela orquestração de outros agentes.
    """
    def __init__(self):
        super().__init__("CEO Nexus", "Agente Principal de Orquestração")
        self.agentes_disponiveis = {}

    def adicionar_agente(self, agente: AgenteIA):
        """Adiciona um agente subordinado ao CEO."""
        self.agentes_disponiveis[agente.nome] = agente

    def executar_tarefa(self, prompt: str):
        """Analisa o prompt do usuário e delega a tarefa."""
        print(f"{self.nome} está analisando o prompt: '{prompt}'")
        
        # Lógica de orquestração do CEO: decide qual agente deve lidar com a tarefa
        if "criar agente" in prompt.lower():
            agente_dev = self.agentes_disponiveis.get("Agente de Desenvolvimento")
            if agente_dev:
                return agente_dev.executar_tarefa(prompt)
            else:
                return "Erro: Agente de Desenvolvimento não encontrado."
        else:
            # Se nenhum agente específico for encontrado, o CEO pede a ajuda do Gemini
            prompt_para_gemini = f"Crie uma resposta detalhada e útil para a solicitação: '{prompt}' no contexto do projeto EcoGuardiões."
            
            if model:
                try:
                    response = model.generate_content(prompt_para_gemini)
                    return response.text
                except Exception as e:
                    return f"Erro ao chamar a API do Gemini: {str(e)}"
            else:
                return "Erro: A API do Gemini não foi configurada. Verifique a variável de ambiente."

class AgenteDesenvolvimento(AgenteIA):
    """
    Agente especializado na geração de código Python.
    """
    def __init__(self):
        super().__init__("Agente de Desenvolvimento", "Desenvolvimento de Código")

    def executar_tarefa(self, descricao_tarefa: str):
        """Gera código Python com base em uma descrição da tarefa."""
        print(f"Agente {self.nome} está recebendo a tarefa: '{descricao_tarefa}'")
        
        prompt = f"Gere o código Python para a seguinte tarefa: {descricao_tarefa}. Responda apenas com o código."
        
        if model:
            try:
                response = model.generate_content(prompt)
                codigo_gerado = response.text
                return f"Código gerado pelo Agente de Desenvolvimento:\n```python\n{codigo_gerado}\n```"
            except Exception as e:
                return f"Erro ao gerar código: {str(e)}"
        else:
            return "Erro: A API do Gemini não foi configurada. Verifique a variável de ambiente."

# ====================================================================
# Função Principal para a Vercel
# ====================================================================
def handler(request):
    """
    Função principal que a Vercel executa para lidar com requisições HTTP.
    Este é o único ponto de entrada para a API.
    """
    if request.method == "POST":
        try:
            body = json.loads(request.body)
            prompt_usuario = body.get("prompt")

            if not prompt_usuario:
                 return {
                    "statusCode": 400,
                    "body": json.dumps({"error": "O prompt é obrigatório."}),
                    "headers": {"Content-Type": "application/json"}
                }
            
            # --- Lógica Principal de Orquestração ---
            # O CEO Nexus é o ponto de entrada da nossa lógica de agentes.
            ceo_nexus = CEONexus()
            agente_dev = AgenteDesenvolvimento()
            ceo_nexus.adicionar_agente(agente_dev)
            
            resposta_do_agente = ceo_nexus.executar_tarefa(prompt_usuario)

            return {
                "statusCode": 200,
                "body": json.dumps({"response": resposta_do_agente}),
                "headers": {"Content-Type": "application/json"}
            }

        except Exception as e:
            # Tratamento de erro genérico para qualquer falha na execução
            return {
                "statusCode": 500,
                "body": json.dumps({"error": f"Erro interno do servidor: {str(e)}"}),
                "headers": {"Content-Type": "application/json"}
            }

    return {
        "statusCode": 405,
        "body": "Método não permitido.",
        "headers": {"Content-Type": "text/plain"}
    }

