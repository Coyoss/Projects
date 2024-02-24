#!/usr/bin/python3

def decrypt_message(encrypted_message, shift):
    decrypted_message = ""
    for char in encrypted_message:
        if char.isalpha():  # Verifica se o caractere é uma letra
            shifted = ord(char) - shift
            if char.islower():  # Verifica se o caractere é minúsculo
                if shifted < ord('a'):
                    shifted += 26
            elif char.isupper():  # Verifica se o caractere é maiúsculo
                if shifted < ord('A'):
                    shifted += 26
            decrypted_message += chr(shifted)
        else:
            decrypted_message += char
    return decrypted_message

def main():
    encrypted_message = input("Digite a mensagem criptografada: ")
    shift = int(input("Digite o número de posições para deslocamento: "))
    decrypted_message = decrypt_message(encrypted_message, shift)
    print("Mensagem descriptografada:", decrypted_message)

if __name__ == "__main__":
    main()
