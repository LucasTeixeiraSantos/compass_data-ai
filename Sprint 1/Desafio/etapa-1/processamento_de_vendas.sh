#!/bin/bash

DATA_ATUAL=$(date +%Y%m%d)
DATA_FORMATADA=$(date +%Y/%m/%d\ %H:%M)
DIR_BASE="/home/lucas-ubuntu/ecommerce"
DIR_VENDAS="${DIR_BASE}/vendas"
DIR_BACKUP="${DIR_VENDAS}/backup"
CSV="${DIR_BASE}/dados_de_vendas.csv"
CSV_BACKUP="${DIR_BACKUP}/dados-${DATA_ATUAL}.csv"
CSV_BACKUP_RENOMEADO="${DIR_BACKUP}/backup-dados-${DATA_ATUAL}.csv"
RELATORIO="${DIR_BACKUP}/relatorio-${DATA_ATUAL}.txt"

comando_existe() {
    command -v "$1" >/dev/null 2>&1
}

verificar_comandos() {
    local comandos=("cp" "mv" "awk" "sort" "uniq" "wc" "head" "zip")
    for cmd in "${comandos[@]}"; do
        if ! comando_existe "$cmd"; then
            echo "Erro: O comando '$cmd' não está instalado." >&2
            exit 1
        fi
    done
}

preparar_diretorios() {
    mkdir -p "$DIR_VENDAS" "$DIR_BACKUP" || { echo "Erro ao criar diretórios"; exit 1; }
    cp "$CSV" "$DIR_VENDAS/" || { echo "Erro ao copiar $CSV para $DIR_VENDAS"; exit 1; }
    cp "$DIR_VENDAS/$(basename "$CSV")" "$CSV_BACKUP" || { echo "Erro ao copiar $(basename "$CSV") para $CSV_BACKUP"; exit 1; }
    mv "$CSV_BACKUP" "$CSV_BACKUP_RENOMEADO" || { echo "Erro ao renomear $CSV_BACKUP para $CSV_BACKUP_RENOMEADO"; exit 1; }
    echo "Diretórios preparados com sucesso"
}

extrair_informacoes() {
    local data_primeiro_registro data_ultimo_registro itens_diferentes
    data_primeiro_registro=$(awk -F, 'NR==2 {print $5}' "$CSV_BACKUP_RENOMEADO")
    data_ultimo_registro=$(awk -F, 'END {print $5}' "$CSV_BACKUP_RENOMEADO")
    itens_diferentes=$(awk -F, 'NR>1 {print $2}' "$CSV_BACKUP_RENOMEADO" | sort | uniq | wc -l)
    
    echo "$data_primeiro_registro" "$data_ultimo_registro" "$itens_diferentes"
    echo "Extração realizada com sucesso"
}

criar_relatorio() {
    local data_primeiro_registro="$1"
    local data_ultimo_registro="$2"
    local itens_diferentes="$3"

    {
        echo "Data do sistema operacional: ${DATA_FORMATADA}"
        echo "Data do primeiro registro de venda: ${data_primeiro_registro}"
        echo "Data do último registro de venda: ${data_ultimo_registro}"
        echo "Quantidade total de itens diferentes vendidos: ${itens_diferentes}"
        echo "Primeiras 10 linhas do arquivo ${CSV_BACKUP_RENOMEADO}:"
        head -n 10 "$CSV_BACKUP_RENOMEADO"
    } > "$RELATORIO" || { echo "Erro ao criar o relatório em $RELATORIO"; exit 1; }
    echo "Relatório criado com sucesso"
}

comprimir_backup() {
    (cd "$DIR_BACKUP" && zip -j "backup-dados-${DATA_ATUAL}.zip" "backup-dados-${DATA_ATUAL}.csv") || { echo "Erro ao comprimir $CSV_BACKUP_RENOMEADO"; exit 1; }
    echo "Compressão realizada com sucesso"
}

limpar_arquivos() {
    rm "$CSV_BACKUP_RENOMEADO" "$DIR_VENDAS/$(basename "$CSV")" || { echo "Erro ao remover arquivos"; exit 1; }
    echo "Limpeza realizada com sucesso"
}

main() {
    verificar_comandos
    preparar_diretorios
    IFS=" " read -r data_primeiro_registro data_ultimo_registro itens_diferentes < <(extrair_informacoes)
    criar_relatorio "$data_primeiro_registro" "$data_ultimo_registro" "$itens_diferentes"
    comprimir_backup
    limpar_arquivos
    echo "Processamento de vendas concluído com sucesso às ${DATA_FORMATADA}."
}

main
