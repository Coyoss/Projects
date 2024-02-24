#!/usr/bin/phyton3
def encrypt_message(message, shift):
    encrypted_message = ""
    for char in message:
        if char.isalpha():  # Verifica se o caractere é uma letra
            shifted = ord(char) + shift
            if char.islower():  # Verifica se o caractere é minúsculo
                if shifted > ord('z'):
                    shifted -= 26
            elif char.isupper():  # Verifica se o caractere é maiúsculo
                if shifted > ord('Z'):
                    shifted -= 26
            encrypted_message += chr(shifted)
        else:
            encrypted_message += char
    return encrypted_message

def main():
    message = input("Digite a mensagem a ser criptografada: ")
    shift = int(input("Digite o número de posições para deslocamento: "))
    encrypted_message = encrypt_message(message, shift)
    print("Mensagem criptografada:", encrypted_message)

if __name__ == "__main__":
    main()

