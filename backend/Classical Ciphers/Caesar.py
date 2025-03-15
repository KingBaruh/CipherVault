from abc import ABC

from backend.Cipher import Cipher


class CaesarCipher(Cipher):
    def __init__(self, key):
        self.key = key

    def getKey(self):
        return self.key

    def setKey(self, key):
        self.key = key

    def encrypt(self, text: str) -> str:
        return self.coded(text, self.key)

    def decrypt(self, text: str) -> str:
        return self.coded(text, 26 - self.key)

    def coded(self, text: str, key) -> str:
        result = ''
        for char in text:

            if char.isalpha():
                # Encrypt/Dcrypt uppercase characters
                if char.isupper():
                    result += chr((ord(char) + key - 65) % 26 + 65)

                # Encrypt/Dcrypt lowercase characters
                else:
                    result += chr((ord(char) + key - 97) % 26 + 97)
            else:
                result += char

        return result

