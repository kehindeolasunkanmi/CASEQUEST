# ==========================================================
# CaseQuest Secure Cipher System
# File: ciphers.py
# Purpose: Traditional Cryptographic Algorithms
# ==========================================================


# ==========================================================
# Caesar Cipher
# ==========================================================

def caesar_encrypt(text, key):
    result = ""

    for char in text:
        if char.isalpha():

            if char.isupper():
                result += chr((ord(char) - 65 + key) % 26 + 65)

            else:
                result += chr((ord(char) - 97 + key) % 26 + 97)

        else:
            result += char

    return result


def caesar_decrypt(text, key):
    return caesar_encrypt(text, -key)


# ==========================================================
# Additive Cipher
# ==========================================================

def additive_encrypt(text, key):
    result = ""

    for char in text:
        if char.isalpha():

            if char.isupper():
                result += chr((ord(char) - 65 + key) % 26 + 65)

            else:
                result += chr((ord(char) - 97 + key) % 26 + 97)

        else:
            result += char

    return result


def additive_decrypt(text, key):
    return additive_encrypt(text, -key)


# ==========================================================
# Vigenere Cipher
# ==========================================================

def vigenere_encrypt(text, key):

    result = ""

    key = key.upper()

    key_index = 0


    for char in text:

        if char.isalpha():

            shift = ord(key[key_index % len(key)]) - ord('A')

            encrypted = chr(
                (ord(char.upper()) - ord('A') + shift) % 26
                + ord('A')
            )

            result += encrypted

            key_index += 1

        else:

            result += char


    return result



def vigenere_decrypt(text, key):

    result = ""

    key = key.upper()

    key_index = 0


    for char in text:

        if char.isalpha():

            shift = ord(key[key_index % len(key)]) - ord('A')

            decrypted = chr(
                (ord(char.upper()) - ord('A') - shift) % 26
                + ord('A')
            )

            result += decrypted

            key_index += 1

        else:

            result += char


    return result


# ==========================================================
# Affine Cipher
# Encryption Formula:
# E(x) = (ax + b) mod 26
# ==========================================================

def modular_inverse(a, m):
    for i in range(m):
        if (a * i) % m == 1:
            return i

    return None


def affine_encrypt(text, a, b):

    result = ""

    for char in text:

        if char.isalpha():

            if char.isupper():
                x = ord(char) - 65
                result += chr(((a * x + b) % 26) + 65)

            else:
                x = ord(char) - 97
                result += chr(((a * x + b) % 26) + 97)

        else:
            result += char

    return result


def affine_decrypt(text, a, b):

    result = ""

    inverse = modular_inverse(a, 26)

    if inverse is None:
        return "Invalid Key: 'a' has no modular inverse"


    for char in text:

        if char.isalpha():

            if char.isupper():
                x = ord(char) - 65
                result += chr((inverse * (x - b) % 26) + 65)

            else:
                x = ord(char) - 97
                result += chr((inverse * (x - b) % 26) + 97)

        else:
            result += char

    return result