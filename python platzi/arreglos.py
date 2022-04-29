

def run():
    numero = [1,2,3,4]
    # Agregar un valor
    numero.append(6);
    # Eliminar por posición
    numero.pop(1)

    # Recorrer arreglos
    for element in numero:
        print(element)
    # Concatenar listas 
    arreglo_final = numero + [5,6,7,8]
    print("Arreglo concatenado %a"%(arreglo_final))

    # Multiplicar arreglos
    print("Arreglo multiplicado por 5: %s" % (numero*5))
    # Slice
    print("Slice: %s"%(str(numero[1:3])))

    print("Array invertido %s" % (str(numero[::-1])))
    
    print("Array Original %s"%(numero))

    # Tuplas
    # Son las constantes de los arreglos, son inmutables. No consumen tanta al contrario de las listas
    mi_tupla = (1,2,3,4)
    print(mi_tupla)
# Punto de entrada de cualquien aplicación de python
if __name__ == "__main__":
    run()