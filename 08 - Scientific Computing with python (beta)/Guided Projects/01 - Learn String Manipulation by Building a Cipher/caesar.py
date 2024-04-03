def caesar(message, offset, direction):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    final_text = ''

    for char in message.lower():
        if not char.isalpha():
            final_text += char
        else:
            index = alphabet.find(char)
            new_index = (index + direction* offset) % len(alphabet)
            final_text += alphabet[new_index]
    return final_text


def encrypt(message, offset):
    return caesar(message, offset, 1)


def decrypt(message, offset):
    return caesar(message, offset, -1)