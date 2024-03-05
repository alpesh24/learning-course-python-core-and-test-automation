class Cipher:
    def __init__(self, keyword):
        self.keyword = keyword.upper()
        self.alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.ciper_alphabet = self.generate_cipher_alphabet()

    def generate_cipher_alphabet(self):
        unique_keyword = ""
        for char in self.keyword:
            if char not in unique_keyword and char.isalpha():
                unique_keyword+=char
        remaining_letters = [char for char in self.alphabet if char not in unique_keyword]

        return unique_keyword + "".join(remaining_letters)

    def encode(self, data):
        encoded_text = ""
        for char in data:
            if char.isalpha():
                idx= self.alphabet.find(char.upper())
                if char.isupper():
                    encoded_text += self.ciper_alphabet[idx] if idx!=-1 else char
                else:
                    encoded_text += self.ciper_alphabet[idx].lower() if idx!=-1 else char
            else:
                encoded_text +=char
        return encoded_text    
    
    def decode(self, data):
        decoded_text = ""
        for char in data:
            if char.isalpha():
                idx = self.ciper_alphabet.find(char.upper())
                if char.isupper():
                    decoded_text += self.alphabet[idx] if idx!=-1 else char
                else:
                    decoded_text += self.alphabet[idx].lower() if idx!=-1 else char
            else:
                decoded_text+=char
        return decoded_text
    
cipher = Cipher("crypto")
print(cipher.encode("Hello world"))

print(cipher.decode("Fjedhc dn atidsn"))