import sys

def rectangle(x, y, letra='A'):
    if x == 1 and y == 1:
        if letra == 'A': print('o')
        elif letra == 'B': print('B')
        elif letra == 'C': print('O')
        return

    if x <= 1 or y <= 1:
        return

    if letra == 'A':
        esquina, h_borde, v_borde, relleno = 'o', '-', '|', ' '
    elif letra == 'B':
        esquina, h_borde, v_borde, relleno = 'B', '/', '/', ' '
    elif letra == 'C':
        for fila in range(y):
            linea = ""
            for columna in range(x):
                es_esquina = (fila == 0 or fila == y - 1) and (columna == 0 or columna == x - 1)
                es_borde_h = (fila == 0 or fila == y - 1) and (0 < columna < x - 1)
                es_borde_v = (0 < fila < y - 1) and (columna == 0 or columna == x - 1)
                
                if es_esquina:
                    linea += 'O'
                elif es_borde_h:
                    linea += 'x' if columna % 2 != 0 else 'A'
                elif es_borde_v:
                    linea += 'x' if fila % 2 != 0 else 'A'
                else:
                    linea += 'O' if (fila + columna) % 2 == 0 else 'B'
            print(linea)
        return
    else:
        print("Letra no reconocida. A de ser: A, B o C")
        return

    for fila in range(y):
        if fila == 0 or fila == y - 1:
            print(esquina + h_borde * (x - 2) + esquina)
        else:
            print(v_borde + relleno * (x - 2) + v_borde)

def main():
    if len(sys.argv):
        try:
            x = int(sys.argv[1])
            y = int(sys.argv[2])
            
            letra = sys.argv[3].upper() if len(sys.argv) == 4 else 'A'
            
            rectangle(x, y, letra)
        except ValueError:
            print("Los dos primeros argumentos deben ser números enteros")
    else:
        print("Uso: python play_game.py <ancho> <alto> [tipo: A, B o C]")   

if __name__ == "__main__":
    main()