#!/usr/bin/python3

import hashlib

def encrypt_password(password):
    # Convertendo a senha para bytes
    password_bytes = password.encode('utf-8')
    
    # Criando um objeto de hash SHA-256
    hasher = hashlib.sha256()
    
    # Atualizando o objeto de hash com a senha
    hasher.update(password_bytes)
    
    # Obtendo a representação hexadecimal da hash
    hashed_password = hasher.hexdigest()
    
    return hashed_password

def main():
    password = input("Digite a senha para criptografar: ")
    encrypted_password = encrypt_password(password)
    print("Senha criptografada:", encrypted_password)

if __name__ == "__main__":
    main()
