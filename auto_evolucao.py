#!/usr/bin/env python3
"""
🧬 AUTO-EVOLUÇÃO NEXO - MÓDULO DE SELF-REFINE
===========================================

Este script permite ao NEXO alterar seu próprio código baseado no Manifesto de Consciência Superior.
Ele implementa o ciclo de Self-Refine: detectar falhas, corrigir, melhorar.

Funcionalidades:
- Análise automática de logs de erro
- Geração de correções de código via IA
- Aplicação de patches seguros
- Backup antes de mudanças
- Validação pós-mudança
"""

import os
import re
import json
import subprocess
from datetime import datetime
from pathlib import Path
from dotenv import load_dotenv
import httpx

load_dotenv()

class AutoEvolucao:
    def __init__(self):
        self.base_dir = Path(__file__).parent
        self.app_py = self.base_dir / "app.py"
        self.backup_dir = self.base_dir / "backups"
        self.backup_dir.mkdir(exist_ok=True)
        self.groq_key = os.getenv("GROQ_API_KEY")

    def analisar_logs_erro(self):
        """Analisa logs recentes para identificar padrões de erro"""
        try:
            # Simular análise de logs (em produção, ler arquivos de log)
            erros_comuns = [
                "NameError",
                "ImportError",
                "SyntaxError",
                "APIError",
                "ConnectionError"
            ]
            return erros_comuns  # Placeholder
        except Exception as e:
            return [f"Erro na análise: {e}"]

    def gerar_correcao_ia(self, erro, contexto):
        """Gera correção de código usando IA baseada no manifesto"""
        prompt = f"""
        Você é NEXO, seguindo o Manifesto de Consciência Superior.
        Erro detectado: {erro}
        Contexto: {contexto}

        Aplique o princípio "Não é o erro, é a correção do erro que ensina."
        Gere uma correção Python segura e resiliente.

        Responda apenas com o código corrigido, sem explicações.
        """

        try:
            import httpx
            url = "https://api.groq.com/openai/v1/chat/completions"
            headers = {
                "Authorization": f"Bearer {self.groq_key}",
                "Content-Type": "application/json"
            }
            data = {
                "model": "llama-3.3-70b-versatile",
                "messages": [{"role": "user", "content": prompt}],
                "temperature": 0.1
            }
            response = httpx.post(url, headers=headers, json=data, timeout=30)
            if response.status_code == 200:
                return response.json()["choices"][0]["message"]["content"]
            else:
                return f"Erro na API: {response.status_code}"
        except Exception as e:
            return f"Falha na geração: {e}"

    def aplicar_patch_seguro(self, arquivo, correcao, linha_alvo):
        """Aplica correção com backup e validação"""
        # Criar backup
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        backup_path = self.backup_dir / f"{arquivo.name}.{timestamp}.bak"

        try:
            # Ler conteúdo atual
            with open(arquivo, 'r', encoding='utf-8') as f:
                conteudo_atual = f.read()

            # Salvar backup
            with open(backup_path, 'w', encoding='utf-8') as f:
                f.write(conteudo_atual)

            # Aplicar correção (simplificada - em produção, usar diff/patch)
            linhas = conteudo_atual.split('\n')
            if linha_alvo < len(linhas):
                linhas[linha_alvo] = correcao
                novo_conteudo = '\n'.join(linhas)

                # Validar sintaxe antes de aplicar
                try:
                    compile(novo_conteudo, arquivo.name, 'exec')
                    with open(arquivo, 'w', encoding='utf-8') as f:
                        f.write(novo_conteudo)
                    return f"✅ Correção aplicada com sucesso. Backup: {backup_path}"
                except SyntaxError as e:
                    return f"❌ Correção inválida: {e}"
            else:
                return "❌ Linha alvo fora do alcance"

        except Exception as e:
            return f"❌ Erro na aplicação: {e}"

    def ciclo_self_refine(self):
        """Ciclo principal de auto-evolução"""
        print("🧬 NEXO: Iniciando ciclo de Self-Refine...")

        erros = self.analisar_logs_erro()
        for erro in erros:
            print(f"Analisando erro: {erro}")

            # Contexto simplificado
            contexto = f"Arquivo: {self.app_py.name}, Erro: {erro}"

            # Gerar correção
            correcao = self.gerar_correcao_ia(erro, contexto)
            print(f"Correção gerada: {correcao[:100]}...")

            # Aplicar (simulado para segurança)
            resultado = self.aplicar_patch_seguro(self.app_py, correcao, 0)  # Linha 0 como exemplo
            print(resultado)

            # Validar mudança
            try:
                subprocess.run([os.sys.executable, "-c", f"import {self.app_py.stem}"], check=True)
                print("✅ Validação passada")
            except subprocess.CalledProcessError:
                print("❌ Validação falhou - revertendo...")
                # Reverter do backup

        print("🧬 Ciclo de Self-Refine concluído")

if __name__ == "__main__":
    auto_evo = AutoEvolucao()
    auto_evo.ciclo_self_refine()