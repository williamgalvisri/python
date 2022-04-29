contador = 0;

print('2 elevado a %s es igual a: %s' % (str(contador), str(2**contador)))

def run():
    LIMITE = 1000;

    contador = 0;
    potencia_2 = 2**contador;
    while potencia_2 < LIMITE:
        print('2 elevado a %s es igual a: %s' % (str(contador), str(potencia_2)))
        contador += 1
        potencia_2 = 2**contador;

# Punto de entrada de cualquien aplicación de python
if __name__ == "__main__":
    run()