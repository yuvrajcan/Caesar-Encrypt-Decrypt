def caesar_encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            shift_base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            result += char
    return result

def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)

text = "Hello"
shift = 3
encrypted = caesar_encrypt(text, shift)
decrypted = caesar_decrypt(encrypted, shift)
print(f"Original: {text}")
print(f"Encrypted: {encrypted}")
print(f"Decrypted: {decrypted}")
