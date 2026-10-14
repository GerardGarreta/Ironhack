def es_congruente(a, b, n):
  
  # Verifica si 'a' es congruente con 'b' módulo 'n'.
  
  if n == 0:
    raise ValueError("El módulo no puede ser cero.")
  return (a - b) % n == 0


def comprobar_congruencia():
    
  
  print("")    
  print("COMPROBADOR DE CONGRUENCIAS MODULARES")
  print("")    
  
  try:
    
    # Introdución de datos
    
    a = int(input("Introduce el primer número (a): "))
    b = int(input("Introduce el segundo número (b): "))
    n = int(input("Introduce el módulo (n): "))

    if n == 0:
      print(
          "\n[Error]: El módulo no puede ser cero."
      )
      return

    # Función lógica
    
    resultado = es_congruente(a, b, n)

    # Desglose y explicación matemática
    
    print("\n")
    print(f"ANÁLISIS MATEMÁTICO: {a} ≡ {b} (mod {n})")
    print("")

    resto_a = a % n
    resto_b = b % n
    diferencia = a - b

    print(f"1. Comparación de restos al dividir entre {n}:")
    print("")
    print(f"   • {a} mod {n} = {resto_a}")
    print(f"   • {b} mod {n} = {resto_b}")

    print(f"\n2. Comprobación de la diferencia (a - b):")
    print("")
    print(f"   • {a} - {b} = {diferencia}")

    # Conclusión
    
    print("")
    print("3. Resultado:")
    print("")
    
    if resultado:
      k = diferencia // n
      print(
          f" - Sí existe congruencia {a} es congruente con {b} módulo {n}."
      )
      print("")    
      print(f"JUSTIFICACIÓN:")
      print("")    
      print(f"- Dejan el mismo resto ({resto_a})")
      print(f"- La diferencia es múltiplo de {n}:")
      print("")    
      print(f"   • {diferencia} = {n} × ({k})")
    else:
      print(
          f" - NO existe congruencia. {a} NO es congruente con {b} módulo {n}.\n"
      )
      print(
          f"JUSTIFICACIÓN:\n"
          f"\n - Sus restos son diferentes ({resto_a} ≠ {resto_b})"
          f" - La diferencia ({diferencia}) no es un múltiplo exacto de {n}."
      )

  except ValueError:
    print(
        "\n[Error]: Por favor, introduce únicamente números enteros válidos."
    )

if __name__ == "__main__":
  comprobar_congruencia()