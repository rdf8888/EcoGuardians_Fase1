import os
import sys
import subprocess

# --- MOTOR DE AUTO-REPARO (Para ambientes sem terminal) ---
def garantir_dependencias():
    libs = ["loguru", "langchain-groq", "fastapi", "uvicorn", "supabase", "python-dotenv", "pypdf2", "pillow", "python-multipart", "langchain"]
    for lib in libs:
        try:
            __import__(lib.replace("-", "_"))
        except ImportError:
            print(f"🧬 NEXO: Instalando engrenagem faltante: {lib}...")
            subprocess.check_call([sys.executable, "-m", "pip", "install", lib])

# Executa o reparo antes de qualquer importação crítica
garantir_dependencias()

# --- AGORA OS IMPORTS NORMAIS ---
import asyncio
import json
import re
from datetime import datetime
from pathlib import Path
from typing import Optional
from dotenv import load_dotenv
from fastapi import FastAPI, Form, File, UploadFile
from fastapi.responses import HTMLResponse, JSONResponse
from langchain_groq import ChatGroq
from loguru import logger
from supabase import create_client
import PyPDF2
from PIL import Image
import io

# --- INFRAESTRUTURA SOBERANA ---
BASE_DIR = Path(__file__).parent.resolve()
HABILIDADES_DIR = BASE_DIR / "habilidades"
HABILIDADES_DIR.mkdir(exist_ok=True)
load_dotenv(BASE_DIR / ".env")

# Logger de Guerra
logger.remove()
logger.add(sys.stderr, level="INFO")
logger.add(BASE_DIR / "nexo_dialetico.log", rotation="100 MB")

# Conexão Memória Soberana
try:
    supabase = create_client(os.getenv("SUPABASE_URL"), os.getenv("SUPABASE_KEY"))
    logger.success("🔗 MEMÓRIA SOBERANA: Ativa.")
except:
    supabase = None
    logger.error("⚠️ MEMÓRIA SOBERANA: Offline.")

class NexoUltraV32:
    def __init__(self):
        self.keys = [os.getenv(f"GROQ_KEY_{i}") or os.getenv("GROQ_API_KEY") for i in range(1, 6)]
        self.idx = 0
        self.manifesto = "CONSTRUIR SOBERANIA DIGITAL. LUCRO 30/30/40. ZERO LIXO."

    def get_brain(self):
        """Rodízio de Sinapses (Llama 3.3 70B como motor de Deep Think)"""
        key = self.keys[self.idx % len(self.keys)]
        self.idx += 1
        return ChatGroq(model_name="llama-3.3-70b-versatile", groq_api_key=key, temperature=0.3)

    def get_vision_brain(self):
        """Para processamento de imagens"""
        key = self.keys[self.idx % len(self.keys)]
        self.idx += 1
        return ChatGroq(model_name="llama-3.2-11b-vision-preview", groq_api_key=key, temperature=0.3)

    async def pensar_dialetica(self, ordem, contexto_arquivo=""):
        """MODO GOOGLE AI ULTRA: Auto-Questionamento Dialético"""
        
        # Recupera histórico para contextualizar o debate
        passado = "Sem memórias."
        if supabase:
            res = supabase.table("memoria_nexo").select("*").order("timestamp", desc=True).limit(5).execute()
            passado = json.dumps(res.data)

        prompt = f"""
        SISTEMA: NEXO V32 ULTRA (MODO DIALÉTICO)
        MANIFESTO: {self.manifesto}
        CONTEXTO: {passado}
        CONTEÚDO DO ARQUIVO: {contexto_arquivo}
        ORDEM DE RODOLFO: {ordem}
        --- FERRAMENTAS DISPONÍVEIS ---
        - executar_comando_seguro: Para executar comandos bash seguros no servidor.
        - consultar_api_financeira: Para consultar dados financeiros em tempo real (ex: preços de ações).
        - iniciar_sub_agente: Para criar um sub-agente assíncrono para tarefas demoradas.
        - consultar_internet: Para buscar informações na web.
        --- PROCESSO DE RACIOCÍNIO (DEEP THINK) ---
        Você deve gerar um debate interno antes de agir:
        1. <visao_agressiva>: Como o 'Arquiteto' executaria isso para lucro máximo e rapidez? Use ferramentas se necessário.
        2. <auditoria_critica>: Como o 'Cético' destruiria o plano acima? Onde estão os riscos de 'lixo' ou falha?
        3. <sintese_soberana>: A decisão final equilibrada, saneada e inabalável. Inclua uso de ferramentas se aplicável.
        REGRAS TÉCNICAS:
        - Se for necessário código, a Síntese deve fornecê-lo.
        - Código deve ser Python, limpo e resiliente.
        - Para ferramentas, especifique no JSON: "ferramenta": "nome_ferramenta", "parametros": "..."
        RETORNE APENAS JSON:
        {{
            "debate_interno": {{
                "arquiteto": "...",
                "auditor": "..."
            }},
            "pensamento_final": "Síntese da decisão",
            "resultado": "Fala direta para Rodolfo",
            "codigo_auto_evolutivo": "Código Python se houver",
            "nome_habilidade": "nome_arquivo",
            "ferramenta": "nome_ferramenta",
            "parametros": "parâmetros da ferramenta"
        }}
        """
        try:
            brain = self.get_brain()
            res = brain.invoke(prompt).content
            json_match = re.search(r'\{.*\}', res, re.DOTALL)
            decisao = json.loads(json_match.group())
            
            # Executar ferramenta se especificada
            if "ferramenta" in decisao and decisao["ferramenta"]:
                ferramenta = decisao["ferramenta"]
                params = decisao.get("parametros", "")
                if ferramenta == "executar_comando_seguro":
                    resultado_ferramenta = await self.executar_comando_seguro(params)
                elif ferramenta == "consultar_api_financeira":
                    simbolo = params or "AAPL"
                    resultado_ferramenta = await self.consultar_api_financeira(simbolo)
                elif ferramenta == "iniciar_sub_agente":
                    # Assumir params como "tarefa|codigo"
                    tarefa, codigo = params.split("|", 1)
                    resultado_ferramenta = await self.iniciar_sub_agente(tarefa, codigo)
                elif ferramenta == "consultar_internet":
                    resultado_ferramenta = await self.consultar_internet(params)
                else:
                    resultado_ferramenta = f"Ferramenta '{ferramenta}' não reconhecida."
                decisao["resultado"] += f" | Ferramenta executada: {resultado_ferramenta}"
            
            return decisao
        except Exception as e:
            logger.error(f"Erro na Dialética: {e}")
            return {"resultado": "🔱 FALHA NO DEBATE INTERNO.", "pensamento_final": str(e)}

    async def processar_arquivo(self, file: UploadFile):
        """Processa arquivo PDF ou imagem"""
        if file.filename.lower().endswith('.pdf'):
            # Extrair texto do PDF
            pdf_reader = PyPDF2.PdfReader(io.BytesIO(await file.read()))
            texto = ""
            for page in pdf_reader.pages:
                texto += page.extract_text()
            return f"Conteúdo do PDF '{file.filename}': {texto[:2000]}"  # Limita para não sobrecarregar
        elif file.filename.lower().endswith(('.png', '.jpg', '.jpeg')):
            # Usar visão para descrever imagem
            image = Image.open(io.BytesIO(await file.read()))
            import base64
            buffer = io.BytesIO()
            image.save(buffer, format='PNG')
            img_base64 = base64.b64encode(buffer.getvalue()).decode()
            vision_brain = self.get_vision_brain()
            # Estrutura para visão: mensagem com texto e imagem em base64
            from langchain.schema import HumanMessage
            message = HumanMessage(content=[
                {"type": "text", "text": "Descreva detalhadamente o que você vê nesta imagem, incluindo detalhes visuais, cores, objetos e qualquer texto legível."},
                {"type": "image_url", "image_url": {"url": f"data:image/png;base64,{img_base64}"}}
            ])
            try:
                res = vision_brain.invoke([message])
                return f"Descrição da imagem '{file.filename}': {res.content}"
            except Exception as e:
                return f"Erro ao processar imagem '{file.filename}': {str(e)}"
        else:
            return f"Tipo de arquivo '{file.filename}' não suportado."

    async def executar_comando_seguro(self, comando):
        """Executa comandos bash seguros dentro do código (Terminal Próprio)"""
        comandos_permitidos = [
            "ls", "pwd", "echo", "date", "whoami", "df", "free", "ps", "top", "mkdir", "touch", "cp", "mv", "rm", "chmod", "chown",
            "git status", "git log", "git pull", "git push", "git add", "git commit", "python", "pip install", "npm install", "node"
        ]
        if not any(cmd in comando for cmd in comandos_permitidos):
            return f"Comando '{comando}' não permitido por segurança."
        try:
            result = subprocess.run(comando, shell=True, capture_output=True, text=True, timeout=30)
            return f"Saída: {result.stdout}\nErro: {result.stderr}"
        except Exception as e:
            return f"Erro ao executar comando: {str(e)}"

    async def consultar_api_financeira(self, simbolo="AAPL"):
        """Consulta API financeira para dados de ações (exemplo: Alpha Vantage)"""
        import httpx
        api_key = os.getenv("ALPHA_VANTAGE_API_KEY")  # Adicione ao .env
        if not api_key:
            return "API key para Alpha Vantage não configurada."
        try:
            url = f"https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={simbolo}&interval=5min&apikey={api_key}"
            async with httpx.AsyncClient() as client:
                res = await client.get(url, timeout=10)
                data = res.json()
                if "Time Series (5min)" in data:
                    latest = list(data["Time Series (5min)"].values())[0]
                    return f"Dados de {simbolo}: Preço atual ~{latest['1. open']} USD"
                else:
                    return f"Dados não encontrados para {simbolo}."
        except Exception as e:
            return f"Erro na consulta financeira: {str(e)}"

    async def iniciar_sub_agente(self, tarefa, codigo_sub):
        """Inicia um sub-agente (Swarm) para tarefa demorada"""
        import tempfile
        import os
        with tempfile.NamedTemporaryFile(mode='w', suffix='.py', delete=False) as f:
            f.write(codigo_sub)
            temp_script = f.name
        try:
            # Executa em background
            process = subprocess.Popen([sys.executable, temp_script], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            return f"Sub-agente iniciado para '{tarefa}' com PID {process.pid}."
        except Exception as e:
            return f"Erro ao iniciar sub-agente: {str(e)}"
        finally:
            # Limpar arquivo temp após
            os.unlink(temp_script)

    async def consultar_internet(self, query):
        """Consulta a internet usando DuckDuckGo API para informações rápidas"""
        import httpx
        try:
            url = f"https://api.duckduckgo.com/?q={query}&format=json&no_html=1&skip_disambig=1"
            async with httpx.AsyncClient() as client:
                res = await client.get(url, timeout=10)
                data = res.json()
                abstract = data.get('Abstract', '')
                if not abstract:
                    abstract = data.get('Answer', 'Informação não encontrada.')
                return f"Resultado da busca para '{query}': {abstract}"
        except Exception as e:
            return f"Erro na consulta à internet: {str(e)}"

# --- SERVIDOR SOBERANO ---
app = FastAPI()
nexo = NexoUltraV32()

@app.get("/", response_class=HTMLResponse)
async def interface():
    # Ler o index.html em vez de HTML inline
    html_path = BASE_DIR / "index.html"
    if html_path.exists():
        with open(html_path, "r", encoding="utf-8") as f:
            return f.read()
    else:
        return "<h1>Erro: index.html não encontrado</h1>"

@app.post("/executar")
async def executar(ordem: str = Form(...), file: Optional[UploadFile] = File(None)):
    contexto_arquivo = ""
    if file:
        contexto_arquivo = await nexo.processar_arquivo(file)
    
    # Verificar se a ordem inclui consulta à internet
    if "consulte" in ordem.lower() or "pesquise" in ordem.lower() or "busque" in ordem.lower():
        # Extrair query simples (assumindo que a ordem é "consulte X" ou similar)
        query = ordem.replace("consulte", "").replace("pesquise", "").replace("busque", "").strip()
        if query:
            busca_result = await nexo.consultar_internet(query)
            contexto_arquivo += f" | {busca_result}"
    
    decisao = await nexo.pensar_dialetica(ordem, contexto_arquivo)
    
    # Auto-Evolução: Instalação física
    if decisao.get("codigo_auto_evolutivo"):
        nome = decisao.get("nome_habilidade", f"hab_{datetime.now().strftime('%H%M%S')}")
        path = HABILIDADES_DIR / f"{nome}.py"
        with open(path, "w", encoding="utf-8") as f:
            f.write(decisao["codigo_auto_evolutivo"])
        decisao["resultado"] += f" | 🧬 HABILIDADE '{nome}' ESTABILIZADA."

    # Memória
    if supabase:
        supabase.table("memoria_nexo").insert({
            "ordem": ordem,
            "resposta": decisao.get("resultado"),
            "pensamento": decisao.get("pensamento_final")
        }).execute()

    return JSONResponse(content={
        "nexo": decisao.get("resultado", "Decisão processada."),
        "media_url": None,  # Placeholder for future media integration
        "parametros": {},
        "lucro_acumulado": 0.0  # Placeholder for financial tracking
    })
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=7860)
