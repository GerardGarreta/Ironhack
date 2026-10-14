from Crypto.Cipher import ChaCha20

def cifrar_mensaje(plaintext, key, nonce):
    """Cifra un texto plano utilizando ChaCha20."""
    cipher = ChaCha20.new(key=key, nonce=nonce)
    return cipher.encrypt(plaintext)

def descifrar_mensaje(ciphertext, key, nonce):
    """Descifra un texto cifrado utilizando ChaCha20."""
    cipher = ChaCha20.new(key=key, nonce=nonce)
    return cipher.decrypt(ciphertext)

def descifrar_con_seek(ciphertext, key, nonce, offset):
    """Descifra un texto aplicando un desplazamiento (seek) en el keystream."""
    cipher = ChaCha20.new(key=key, nonce=nonce)
    cipher.seek(offset)
    return cipher.decrypt(ciphertext)

def mostrar_teoria():
    """Muestra por consola las preguntas y respuestas teóricas."""
    print(" 1. ¿Cuál es el texto cifrado resultante?")
    print("    -> (Se muestra en la ejecución del cifrado)\n")
    
    print(" 2. ¿Qué tamaño tiene el nonce que has utilizado para cifrar el texto plano?")
    print("    -> 8 bytes (64 bits), según el diseño original de ChaCha20.\n")
    
    print(" 3. ¿Puedes utilizar un nonce de mayor tamaño (ej. 12 bytes o 16 bytes)?")
    print("    -> 12 bytes sí (estándar IETF RFC 7539 / RFC 8439). 16 bytes, no directamente en ChaCha20 estándar (se requeriría XChaCha20 con 24 bytes).\n")
    
    print(" 4. ¿Qué implicaciones de seguridad tiene utilizar un nonce de mayor tamaño?")
    print("    -> Reduce drásticamente la probabilidad de colisión y permite cifrar un volumen masivo de mensajes con la misma clave de forma segura.\n")
    
    print(" 5. ¿Qué riesgos de seguridad existen si se reutiliza la misma clave y el mismo nonce para cifrar dos mensajes diferentes?")
    print("    -> Vulnerabilidad crítica. El flujo de claves (keystream) generado es idéntico, permitiendo revelar los textos planos mediante operaciones XOR.\n")
    
    print(" 6. ¿Qué diferencias existen entre ChaCha20 y ChaCha20-Poly1305 en cuanto a la confidencialidad e integridad?")
    print("    -> ChaCha20 ofrece únicamente confidencialidad. ChaCha20-Poly1305 ofrece confidencialidad e integridad simultáneamente (AEAD).")

def main():
    # Parámetros compartidos
    key = b'z\xe8~"\xcayW\x14g\x18+\x1c+\xf9\x80\x06P\x9ej\x888\xb4G\xdf\xe4\xc50,\x8dY\x80\x19'
    nonce = b"\xd6\x7f6\xc7\xe8i*\xa4"

    print("_" * 100)
    print("\n PARTE 1: Cifrado y Cuestiones Teóricas\n")
    
    plaintext = b"Este es un mensaje secreto que quiero cifrar"
    print(f" - Mensaje para cifrar: {plaintext.decode('utf-8')}\n")

    # Cifrado
    ciphertext = cifrar_mensaje(plaintext, key, nonce)
    print(f" - Texto cifrado resultante: {ciphertext}\n")
    
    # Teoría
    mostrar_teoria()
    print("\n" + "_" * 100 + "\n")

    print(" PARTE 2: Descifrado\n")
    ciphertext_misterioso = b'Ehq0\x83\xcb\x8fo\xab\xed\xd0S\x06\xcc\xbb\xecw\xe9\xec(\x1f\xc5E\xdb\x88\x18`W\xc3yQn\xad3\xec.\x08\x92\x8d\x8e\xbb%\x8f\x1a\xa6\xc9=\x15\x0f5\xaa'
    print(f"- Mensaje cifrado: {ciphertext_misterioso}\n")
    
    decrypted_misterioso = descifrar_mensaje(ciphertext_misterioso, key, nonce)
    print(f"- Texto plano descifrado: {decrypted_misterioso.decode('utf-8', errors='replace')}")

    print("\n" + "_" * 100 + "\n")
    print(" EXTRA: Sincronización del Keystream\n")
    
    received_ct = b"\xad\xe2\x9a[C\xca\xa9\xadn\xf9\xaa)\x13\xc2X\x9e\x89\x19`C\xc4n\x1em\xf8?\xe7|\x0b\xd3\xdc\x8f\xacd\x85\x0c\xb8\xc3'\x1a\x12>"
    synced_plaintext = descifrar_con_seek(received_ct, key, nonce, offset=8)
    
    print("- Método utilizado: cipher_sync.seek(8)")
    print(f"- Texto plano sincronizado: {synced_plaintext.decode('utf-8', errors='replace')}\n")
    print("_" * 100)

if __name__ == "__main__":
    main()