# api/gerar_agente.py

import google.generativeai as genai
import os
import json
from abc import ABC, abstractmethod

# --- Configuração de Segurança da API ---
# A chave é lida de uma variável de ambiente, garantindo a segurança.
API_KEY = os.environ.get("GEMINI_API_KEY")
model = None

if API_KEY:
    model = genai.GenerativeModel("gemini-pro", api_key=API_KEY)

# --- Classes de Agentes (para futuras expansões) ---
class AgenteIA(ABC):
    def __init__(self, nome: str, funcao: str):
        self.nome = nome
        self.funcao = funcao
    
    @abstractmethod
    def executar_tarefa(self):
        pass

class CEONexus(AgenteIA):
    def __init__(self):
        super().__init__("CEO Nexus", "Agente Principal de Orquestração")
        self.agentes_subordinados = []

    def adicionar_agente(self, agente):
        self.agentes_subordinados.append(agente)

    def executar_tarefa(self, prompt: str):
        # A lógica de orquestração do CEO vai aqui na Fase 3
        # Por enquanto, apenas repassa para o Gemini
        pass

# --- Função Principal para a Vercel ---
def handler(request):
    """
    Função principal que a Vercel executa para lidar com requisições HTTP.
    """
    if request.method == "POST":
        if not model:
            return {
                "statusCode": 500,
                "body": json.dumps({"error": "API do Gemini não configurada corretamente."}),
                "headers": {"Content-Type": "application/json"}
            }

        try:
            body = json.loads(request.body)
            prompt = body.get("prompt")

            if not prompt:
                return {
                    "statusCode": 400,
                    "body": json.dumps({"error": "O prompt é obrigatório."}),
                    "headers": {"Content-Type": "application/json"}
                }
            
            # Chama a API do Gemini de forma segura
            response = model.generate_content(prompt)
            codigo_gerado = response.text

            return {
                "statusCode": 200,
                "body": json.dumps({"response": codigo_gerado}),
                "headers": {"Content-Type": "application/json"}
            }

        except Exception as e:
            return {
                "statusCode": 500,
                "body": json.dumps({"error": str(e)}),
                "headers": {"Content-Type": "application/json"}
            }

    return {
        "statusCode": 405,
        "body": "Método não permitido.",
        "headers": {"Content-Type": "text/plain"}
    }
