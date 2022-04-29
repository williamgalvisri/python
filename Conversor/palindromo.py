import re;

def palindromo(palabra):
    # Remover espacios con regex
    palabra = re.sub(r"\s+", "", palabra)
    palabra = palabra.lower()
    if palabra == palabra[::-1]:
        return True;
    else:
        return False;

def run():
    palabra = input("Escribe una palabra: ");
    es_palindromo = palindromo(palabra)
    if es_palindromo:
        print("Es palindromo");
    else: 
        print("No es palindromo");
    

# Punto de entrada de cualquien aplicación de python
if __name__ == "__main__":
    run()