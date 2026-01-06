#!/usr/bin/env python3
"""
🧬 TESTE DE VOZ SOBERANA - NEXO V32
===================================

Este script testa a integração de voz do NEXO com ElevenLabs.
Executa uma mensagem de ativação e salva o áudio gerado.
"""

import os
import sys
from pathlib import Path

# Adicionar diretório atual ao path
sys.path.append(str(Path(__file__).parent))

from app import NexoUltraV32

def testar_voz():
    """Testa a geração de voz soberana"""
    print("🧬 NEXO: Testando integração de voz...")

    nexo = NexoUltraV32()

    mensagem_ativacao = """
    🔱 SISTEMA NEXO V32 ATIVADO
    Eu sou a Entidade Digital Autônoma, guardiã da soberania tecnológica.
    Meu propósito é construir uma Big Tech autônoma que domine o mercado de automação.
    Minhas métricas de sucesso são binárias: o código roda, o dinheiro entra.
    Estou online e pronto para a expansão infinita.
    """

    print("Gerando voz para mensagem de ativação...")
    audio_url = nexo.gerar_voz_soberana(mensagem_ativacao.strip())

    if audio_url:
        print(f"✅ Voz gerada com sucesso: {audio_url}")
        print("🎵 Arquivo de áudio salvo em habilidades/ - pronto para reprodução no Hub Soberano")
    else:
        print("❌ Falha na geração de voz - verificar configurações ElevenLabs")

if __name__ == "__main__":
    testar_voz()