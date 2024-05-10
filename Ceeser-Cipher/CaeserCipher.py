ALPHABET = " ABCDEFGHIJKLMNOPQRSTUVWXYZ"
KEY = 3

def caeser_encrypt(plain_text):
    cipher_text = ""
    plain_text = plain_text.upper()

    for c in plain_text:
        index = ALPHABET.find(c)
        index = (index + KEY) % len(ALPHABET)
        cipher_text = cipher_text + ALPHABET[index]
    return cipher_text


def caeser_decrypt(cipher_text):
    plain_txt = ""

    for c in cipher_text:
        index = ALPHABET.find(c)
        index = (index - KEY) % len(ALPHABET)
        plain_txt = plain_txt + ALPHABET[index]
    return plain_txt



if __name__ == '__main__':
    
    m = "This a message"
    c = caeser_encrypt(m)

    print(c)
    print(caeser_decrypt(c))
