
from flask import Flask, request, jsonify
from flask_cors import CORS
import os
from dotenv import load_dotenv
import openai

# Carregar variáveis do ambiente
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return jsonify({
        "message": "EcoGuardians API - Agente Real via OpenAI",
        "version": "2.0.0",
        "status": "online"
    })

@app.route('/api/ia/testar', methods=['POST'])
def testar_ia():
    data = request.get_json()
    if not data or 'mensagem' not in data:
        return jsonify({"error": "Mensagem não enviada"}), 400

    try:
        resposta = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "Você é um agente especialista do projeto EcoGuardians."},
                {"role": "user", "content": data['mensagem']}
            ]
        )
        conteudo = resposta['choices'][0]['message']['content']
        return jsonify({"resposta": conteudo})

    except Exception as e:
        return jsonify({"error": str(e)}), 500
