from Crypto.Cipher import ChaCha20

print("_" * 100)
print("")
print(" PARTE 1: Cifrado y Cuestiones Teóricas")
print("")

print(" - Mensaje para cifrar: Este es un mensaje secreto que quiero cifrar")

# Parámetros proporcionados
plaintext = b"Este es un mensaje secreto que quiero cifrar"
key = (
    b'z\xe8~"\xcayW\x14g\x18+\x1c+\xf9\x80\x06P\x9ej\x888\xb4G\xdf\xe4\xc50,\x8dY\x80\x19'
)
nonce = b"\xd6\x7f6\xc7\xe8i*\xa4"

# Cifrado
cipher_enc = ChaCha20.new(key=key, nonce=nonce)
ciphertext = cipher_enc.encrypt(plaintext)

print("\n1. ¿Cuál es el texto cifrado resultante?")
print("")
print(" -", ciphertext)

print("\n2. ¿Qué tamaño tiene el nonce que has utilizado para cifrar el texto plano?")
print("")
print(" - 8 bytes (64 bits), según el diseño original de ChaCha20.")

(
    print(
        "\n3. ¿Puedes utilizar un nonce de mayor tamaño (ej. 12 bytes o 16 bytes)?"
    )
)
print("")
print(
    " - 12 bytes sí (estándar IETF RFC 7539 / RFC 8439). 16 bytes, no directamente en ChaCha20 estándar (se requeriría XChaCha20 con 24 bytes)."
)

(
    print(
        "\n4. ¿Qué implicaciones de seguridad tiene utilizar un nonce de mayor tamaño?"
    )
)
print("")
print(
    " - Reduce drásticamente la probabilidad de colisión (reutilización accidental) y permite cifrar un volumen masivo de mensajes con la misma clave de forma segura."
)

(
    print(
        "\n5. ¿Qué riesgos de seguridad existen si se reutiliza la misma clave y el mismo nonce para cifrar dos mensajes diferentes?"
    )
)
print("")
print(
    " - Vulnerabilidad crítica. El flujo de claves (keystream) generado es idéntico, permitiendo que un atacante realice una operación XOR entre los textos cifrados (C1 ^ C2 = P1 ^ P2) para revelar los textos planos o patrones."
)

(
    print(
        "\n6. ¿Qué diferencias existen entre ChaCha20 y ChaCha20-Poly1305 en cuanto a la confidencialidad e integridad de la información?"
    )
)
print("")
print(
    " - ChaCha20 ofrece únicamente confidencialidad. ChaCha20-Poly1305 ofrece confidencialidad e integridad simultáneamente (AEAD) mediante una etiqueta de autenticación (tag) de 16 bytes."
)
print("")

print("\n" + "_" * 100 + "\n")
print("")
print(" PARTE 2: Descifrado")
print("")
print("")

# Descifrado del mensaje proporcionado
ciphertext_misterioso = (
   b'Ehq0\x83\xcb\x8fo\xab\xed\xd0S\x06\xcc\xbb\xecw\xe9\xec(\x1f\xc5E\xdb\x88\x18`W\xc3yQn\xad3\xec.\x08\x92\x8d\x8e\xbb%\x8f\x1a\xa6\xc9=\x15\x0f5\xaa'
)

print("- Mensaje cifrado: ", ciphertext_misterioso)
print("")
cipher_misterioso_dec = ChaCha20.new(key=key, nonce=nonce)
decrypted_misterioso = cipher_misterioso_dec.decrypt(ciphertext_misterioso)
print(
    "- Texto plano descifrado: ",
    decrypted_misterioso.decode("utf-8", errors="replace"),
)


print("")
print("\n" + "_" * 100 + "\n")
print("")
print(" EXTRA: Sincronización del Keystream")
print("")


received_ct = b"\xad\xe2\x9a[C\xca\xa9\xadn\xf9\xaa)\x13\xc2X\x9e\x89\x19`C\xc4n\x1em\xf8?\xe7|\x0b\xd3\xdc\x8f\xacd\x85\x0c\xb8\xc3'\x1a\x12>"
cipher_sync = ChaCha20.new(key=key, nonce=nonce)
cipher_sync.seek(8)  # Nos desplazamos 8 bytes en el flujo de claves
synced_plaintext = cipher_sync.decrypt(received_ct)

print("")
print("- Método utilizado: cipher_sync.seek(8)")
print("")
print("- Texto plano sincronizado:", synced_plaintext.decode("utf-8", errors="replace"))
print("")
print("_" * 100)