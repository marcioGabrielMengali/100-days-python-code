import os
def encrypt(text, shift = 0):
    encrypt_text = []
    for letter in text:
        if ord(letter) != 32:
            encrypt_text.append(chr(ord(letter) + shift))
        else:
            encrypt_text.append(' ')
    return encrypt_text


def decrpyt(text, shift = 0):
    encrypt_text = []
    for letter in text:
        if ord(letter) != 32:
            encrypt_text.append(chr(ord(letter) - shift))
        else:
            encrypt_text.append(' ')
    return encrypt_text

while True:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    os.system('cls')
    if direction == 'encode':
        encrpyt_text = encrypt(text = text,shift = shift)
        print(f"Here's the encoded message: {''.join(encrpyt_text)}")
    elif direction ==  'decode':
        decrpyt_text = decrpyt(text, shift)
        print(f"Here's the decoded message: {''.join(decrpyt_text)}")
    else:
        print('Error')
        continue
 