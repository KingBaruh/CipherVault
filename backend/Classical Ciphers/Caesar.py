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
        """Encrypt the given text"""
        pass

    def decrypt(self, text: str) -> str:
        """Decrypt the given text"""
        pass
