import hashlib

while True:
    entrada = input("Digite uma palavra ou frase para mascarar (Ctrl + C para sair): ")
    hash_entrada = hashlib.sha1(entrada.encode())
    print("Hash SHA-1:", hash_entrada.hexdigest())
