def caesar_encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shift_amount = shift % 26
            if char.islower():
                new_char = chr((ord(char) - ord('a') + shift_amount) % 26 + ord('a'))
            else:
                new_char = chr((ord(char) - ord('A') + shift_amount) % 26 + ord('A'))
            encrypted_text += new_char
        else:
            encrypted_text += char
    return encrypted_text

def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)

# Example Usage
plain_text = "Hello, Samuel"
shift_value = 5
encrypted_text = caesar_encrypt(plain_text, shift_value)
decrypted_text = caesar_decrypt(encrypted_text, shift_value)

print("Encrypted Text:", encrypted_text)
print("Decrypted Text:", decrypted_text)
