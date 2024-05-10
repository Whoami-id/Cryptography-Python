from random import randint

ALPHABET = " ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def random_sequence(text):
    random = []

    for _ in range(len(text)):
        random.append(randint(0, len(ALPHABET)-1))
    
    return random


def encrypt(text, key):
    text = text.upper()
    cipher_text = ""

    for index, char in enumerate(text):
        key_index = key[index]
        char_index = ALPHABET.find(char)
        cipher_text += ALPHABET[(char_index + key_index) % len(ALPHABET)]

    return cipher_text



def decrypt(cipher, key):
    plain = ""

    for index, char in enumerate(cipher):
        key_index = key[index]
        char_index = ALPHABET.find(char)
        plain += ALPHABET[(char_index - key_index) % len(ALPHABET)]
    
    return plain


    

if __name__ == "__main__":
    message = "This is a message"
    seq = random_sequence(message)
    print(message.upper())

    cipher = encrypt(message, seq)
    print(cipher)
    decrypt_txt = decrypt(cipher, seq)
    print(decrypt_txt)