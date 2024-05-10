ALPHABET = " ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def crack_caeser(cipher_text):
    for key in range(len(ALPHABET)):
        plain_txt = ""
        for c in cipher_text:
            index = ALPHABET.find(c)
            index = (index - key) % len(ALPHABET)
            plain_txt = plain_txt + ALPHABET[index]
        print("With key %s, the result is: %s " % (key, plain_txt))



if __name__ == '__main__':
    
    c = "WKLVCDCPHVVDJH"
    crack_caeser(c)
   

