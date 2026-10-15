from Crypto.Cipher import AES

def aes_comparacion_modos(texto_plano, clave_cifrado_128):
    
    # PARTE 1
    print("[ PARTE 1: MODO CTR  (Clave 128 bits)]")
    print("")
    
    # Cifrado en modo CTR
    aes_ctr = AES.new(clave_cifrado_256, AES.MODE_CTR)
    texto_cifrado_ctr = aes_ctr.encrypt(texto_plano)
    nonce = aes_ctr.nonce
    
    print(f" - Texto plano original: {texto_plano} (Longitud: {len(texto_plano)} bytes)")
    print(f" - Nonce utilizado: {nonce}")
    print(f" - Texto cifrado CTR: {texto_cifrado_ctr} (Longitud: {len(texto_cifrado_ctr)} bytes)\n")
    
    # Preguntas y Respuestas Parte 1 por pantalla
    
    print("1. ¿Qué ocurre si intentas cifrar el texto plano en CTR?")
    print("\n - A diferencia de ECB, no ocurre ningún error si intentas cifrar el texto plano directamente sin padding, ya que opera como un cifrado en flujo.")
    print("")
    print("2. ¿Cuál es el tamaño del texto cifrado resultante en CTR?")
    print("\n - El tamaño del texto cifrado es exactamente el mismo que el del texto plano original.\n")
    
    print("_" * 150)
    
    # PARTE 2
    print("")
    print("[ PARTE 2: ECB vs CTR (Clave 256 bits) ]")
    print("")
    
    # Modo ECB con padding
    
    texto_plano_padding = texto_plano
    while len(texto_plano_padding) % 16 != 0:
        texto_plano_padding += b"\x00"
        
    aes_ecb = AES.new(clave_cifrado_256, AES.MODE_ECB)
    texto_cifrado_ecb = aes_ecb.encrypt(texto_plano_padding)
    
    print(f" - Texto con padding (ECB): {texto_plano_padding} (Longitud: {len(texto_plano_padding)} bytes)")
    print(f" - Texto cifrado ECB: {texto_cifrado_ecb} (Longitud: {len(texto_cifrado_ecb)} bytes)")
    print(f" - Texto cifrado CTR: {texto_cifrado_ctr} (Longitud: {len(texto_cifrado_ctr)} bytes)\n")

    # Preguntas y Respuestas Parte 2

    print("\n1. ¿Qué diferencias hay en el tamaño del texto cifrado entre el modo de operación ECB y CTR?")
    
    print("\n - ECB: Requiere padding para ajustar el mensaje a múltiplos de 16 bytes, por lo que el texto cifrado puede ser mayor que el original.")
    print(" - CTR: No requiere padding, por lo que el texto cifrado mantiene exactamente la misma longitud que el texto plano.")


if __name__ == "__main__":
    
    
    clave_cifrado_128 = b'A\x83\xbeU\xd7\xa9b\x18\x85AN0\xbft\xc3\xab'
    
    clave_cifrado_256 = b'A\x83\xbeU\xd7\xa9b\x18\x85AN0\xbft\xc3\xabA\x83\xbeU\xd7\xa9b\x18\x85AN0\xbft\xc3\xab'
    
    mensaje_usuario = input("\nIntroduce un mensaje para Bob: ")
    texto_plano = mensaje_usuario.encode('utf-8')
    
    print("\n")
    aes_comparacion_modos(texto_plano, clave_cifrado_256)