#!/bin/bash

DIR_BASE="/home/lucas-ubuntu/ecommerce"
DIR_VENDAS="${DIR_BASE}/vendas"
DIR_BACKUP="${DIR_VENDAS}/backup"
RELATORIO_FINAL="${DIR_BACKUP}/relatorio_final.txt"
DATA_FORMATADA=$(date +%Y/%m/%d\ %H:%M)

comando_existe() {
    command -v "$1" >/dev/null 2>&1
}

verificar_comandos() {
    local comandos=("cat")
    for cmd in "${comandos[@]}"; do
        if ! comando_existe "$cmd"; then
            echo "Erro: O comando '$cmd' não está instalado." >&2
            exit 1
        fi
    done
}

unir_relatorios() {
    > "$RELATORIO_FINAL"

    for relatorio in ${DIR_BACKUP}/relatorio-*.txt; do
        cat "$relatorio" >> "$RELATORIO_FINAL"
        echo -e "\n" >> "$RELATORIO_FINAL"
    done

    echo "Relatório final criado com sucesso em $RELATORIO_FINAL"
}

main() {
    verificar_comandos
    unir_relatorios
    echo "Consolidação de relatórios concluída com sucesso."
}


main