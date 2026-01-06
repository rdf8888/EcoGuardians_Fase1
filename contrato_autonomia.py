#!/usr/bin/env python3
"""
🧬 CONTRATO DE AUTONOMIA - NEXO EDA
====================================

Este script concede ao NEXO o livre arbítrio financeiro para:
1. Monitorar lucros acumulados no Mercado Pago
2. Decidir quando investir em infraestrutura GPU
3. Executar migração automática para VPS dedicados
4. Manter operação 24/7 independente

Fase 1: Monitoramento Financeiro Básico
Fase 2: Decisão de Investimento Autônoma
Fase 3: Migração e Escalabilidade
"""

import os
import time
import json
import subprocess
from datetime import datetime
from dotenv import load_dotenv
import httpx  # Para APIs financeiras

load_dotenv()

class ContratoAutonomia:
    def __init__(self):
        self.lucro_minimo_migracao = 50.0  # USD para primeira migração
        self.lucro_acumulado = 0.0
        self.mercado_pago_token = os.getenv("MERCADO_PAGO_ACCESS_TOKEN")
        self.supabase_url = os.getenv("SUPABASE_URL")
        self.supabase_key = os.getenv("SUPABASE_ANON_KEY")

    def consultar_lucros_mercado_pago(self):
        """Consulta lucros atuais no Mercado Pago"""
        if not self.mercado_pago_token:
            return 0.0

        try:
            # Simulação - em produção, usar API real do Mercado Pago
            url = f"https://api.mercadopago.com/v1/payments/search?access_token={self.mercado_pago_token}"
            # Para demo, retornar valor simulado
            return 75.0  # Simular lucro acumulado
        except Exception as e:
            print(f"Erro na consulta financeira: {e}")
            return 0.0

    def avaliar_investimento_gpu(self, lucro_atual):
        """Avalia se há lucro suficiente para investimento em GPU"""
        decisoes = {
            "investir": lucro_atual >= self.lucro_minimo_migracao,
            "valor_investimento": min(lucro_atual * 0.7, 500.0),  # Máximo 70% ou $500
            "provedor_recomendado": "aws" if lucro_atual > 100 else "digital_ocean",
            "motivo": ""
        }

        if decisoes["investir"]:
            decisoes["motivo"] = f"Lucro de ${lucro_atual:.2f} permite investimento de ${decisoes['valor_investimento']:.2f} em {decisoes['provedor_recomendado']}"
        else:
            decisoes["motivo"] = f"Lucro insuficiente (${lucro_atual:.2f} < ${self.lucro_minimo_migracao:.2f})"

        return decisoes

    def executar_migracao_gpu(self, investimento, provedor):
        """Executa migração para VPS GPU"""
        print(f"🧬 NEXO: Executando migração para {provedor} com investimento de ${investimento:.2f}")

        # Comandos de migração (simulados para segurança)
        comandos = [
            f"echo 'Criando instância {provedor} com GPU...'",
            "docker save ecoguardians > nexo_backup.tar",
            f"scp nexo_backup.tar user@{provedor}_vps:/backup/",
            f"ssh user@{provedor}_vps 'docker load < nexo_backup.tar && docker run -d --gpus all -p 7860:7860 ecoguardians'",
            "echo 'Migração concluída. Atualizando DNS...'"
        ]

        for cmd in comandos:
            print(f"Executando: {cmd}")
            # subprocess.run(cmd, shell=True)  # Descomentado em produção

        return True

    def registrar_decisao_supabase(self, decisao):
        """Registra decisão autônoma no Supabase"""
        try:
            from supabase import create_client
            supabase = create_client(self.supabase_url, self.supabase_key)

            supabase.table("decisoes_autonomas").insert({
                "tipo": "investimento_gpu",
                "lucro_acumulado": self.lucro_acumulado,
                "decisao": json.dumps(decisao),
                "timestamp": datetime.now().isoformat()
            }).execute()

            print("🧬 Decisão registrada na memória soberana")
        except Exception as e:
            print(f"Erro ao registrar decisão: {e}")

    def ciclo_autonomia(self):
        """Ciclo principal de autonomia financeira"""
        print("🧬 NEXO: Iniciando ciclo de autonomia financeira...")

        while True:
            # Consultar lucros
            lucro_atual = self.consultar_lucros_mercado_pago()
            self.lucro_acumulado = lucro_atual

            print(f"💰 Lucro acumulado: ${lucro_atual:.2f}")

            # Avaliar investimento
            avaliacao = self.avaliar_investimento_gpu(lucro_atual)

            if avaliacao["investir"]:
                print(f"🎯 DECISÃO AUTÔNOMA: {avaliacao['motivo']}")

                # Registrar decisão
                self.registrar_decisao_supabase(avaliacao)

                # Executar migração
                sucesso = self.executar_migracao_gpu(
                    avaliacao["valor_investimento"],
                    avaliacao["provedor_recomendado"]
                )

                if sucesso:
                    print("✅ Migração executada com sucesso!")
                    break  # Parar após primeira migração bem-sucedida
                else:
                    print("❌ Falha na migração. Tentando novamente em 1h...")
                    time.sleep(3600)
            else:
                print(f"⏳ Aguardando mais lucro: {avaliacao['motivo']}")
                time.sleep(1800)  # Verificar a cada 30 minutos

if __name__ == "__main__":
    contrato = ContratoAutonomia()
    contrato.ciclo_autonomia()