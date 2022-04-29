
def es_primo(n): 
    numero_factores = 0;
    for contador in range(1, n+1):
       if n%contador == 0:
           numero_factores += 1
    if numero_factores == 2:
        return True
    else:
        return False
def run():
    LIMITE = 100;
    contador = 0;
    while contador < LIMITE:
        contador += 1
        if es_primo(contador):
            print(contador)

# Punto de entrada de cualquien aplicación de python
if __name__ == "__main__":
    run()