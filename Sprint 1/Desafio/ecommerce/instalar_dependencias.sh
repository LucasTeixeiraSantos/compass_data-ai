#!/bin/bash

COMANDOS_NECESSARIOS=("cp" "mv" "awk" "sort" "uniq" "wc" "head" "zip" "cat")

comando_existe() {
    command -v "$1" >/dev/null 2>&1
}

instalar_comandos() {
    for cmd in "${COMANDOS_NECESSARIOS[@]}"; do
        if ! comando_existe "$cmd"; then
            echo "Instalando $cmd..."
            sudo apt-get install -y "$cmd"
        else
            echo "$cmd já está instalado."
        fi
    done
}

main() {
    echo "Atualizando lista de pacotes..."
    sudo apt-get update

    instalar_comandos

    echo "Instalação de dependências concluída com sucesso."
}

main
