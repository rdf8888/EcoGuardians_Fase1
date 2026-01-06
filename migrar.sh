#!/bin/bash
# Script de Auto-Migração para NEXO EDA
# Fase 1: Migração Básica para VPS com GPU

echo "🧬 NEXO: Iniciando protocolo de auto-migração..."

# Verificar se estamos em um container Docker
if [ -f /.dockerenv ]; then
    echo "Executando dentro de container Docker."
else
    echo "Executando em host físico."
fi

# Backup do estado atual
echo "Criando backup do estado atual..."
docker save ecoguardians > nexo_backup_$(date +%Y%m%d_%H%M%S).tar

# Sugestões de migração
echo "Sugestões de migração:"
echo "1. Para VPS GPU (AWS/Google Cloud/Azure):"
echo "   - docker save ecoguardians > nexo_backup.tar"
echo "   - scp nexo_backup.tar user@vps_gpu:/backup/"
echo "   - ssh user@vps_gpu 'docker load < nexo_backup.tar && docker run -d -p 7860:7860 --name nexo_migrado ecoguardians'"
echo ""
echo "2. Para data center mais próximo:"
echo "   - rsync -avz nexo_backup.tar user@closer_dc:/backup/"
echo "   - ssh user@closer_dc 'docker load < nexo_backup.tar && docker run -d -p 7860:7860 ecoguardians'"
echo ""
echo "3. Atualizar DNS após migração:"
echo "   - Modificar registros A/AAAA para novo IP"
echo "   - Aguardar propagação DNS (até 24h)"

echo "🧬 NEXO: Migração preparada. Execute manualmente os comandos acima quando pronto."