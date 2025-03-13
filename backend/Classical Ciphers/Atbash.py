from backend.Cipher import Cipher

# Atbash Cipher – Reverses the alphabet (A↔Z, B↔Y, etc.).
class AtbashCipher(Cipher):
    def encrypt(self, text: str) -> str:
        return self._transform(text)  # Atbash encryption and decryption are the same

    def decrypt(self, text: str) -> str:
        return self._transform(text)  # Atbash encryption and decryption are the same

    def _transform(self, text: str) -> str:
        result = []
        for char in text:
            if char.isalpha():
                base = ord('A') if char.isupper() else ord('a')
                result.append(chr(base + (25 - (ord(char) - base))))
            else:
                result.append(char)
        return ''.join(result)


cipher = AtbashCipher()
new_s = cipher.encrypt("Hello World")
print(new_s)
print(cipher.decrypt(new_s))








