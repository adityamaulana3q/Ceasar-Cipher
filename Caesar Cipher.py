# -*- coding: utf-8 -*-
"""
Created on Fri Oct  3 08:57:01 2025

@author: adity
"""

def caesar_cipher(text, shift, mode='encrypt'):
    result = ""

    # Jika mode dekripsi, geser ke arah sebaliknya
    if mode == 'decrypt':
        shift = -shift

    for char in text:
        if char.isalpha():
            # Tentukan batas ASCII untuk huruf besar atau kecil
            base = ord('A') if char.isupper() else ord('a')
            # Geser dengan rumus modular
            new_char = chr((ord(char) - base + shift) % 26 + base)
            result += new_char
        else:
            # Biarkan karakter non-alfabet
            result += char

    return result

# Contoh penggunaan
print ("====ini adalah program caesar chiper sederhana====")
print ("==================================================")
if __name__ == "__main__":
    text = input("Masukkan teks: ")
    shift = int(input("Masukkan kunci (1-25): "))
    mode = input("Mode (encrypt/decrypt): ").strip().lower()

    if mode not in ['encrypt', 'decrypt']:
        print("Mode tidak valid! Pilih 'encrypt' atau 'decrypt'.")
    else:
        output = caesar_cipher(text, shift, mode)
        print(f"Hasil ({mode}): {output}")
