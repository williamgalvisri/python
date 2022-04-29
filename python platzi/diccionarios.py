def run():
    mi_diccionario = {
        'key1': 1,
        'key2': 2,
        'key3': [3, 4, 5] 
    }
    print(mi_diccionario)
    print(mi_diccionario['key1'])

    for key, value in mi_diccionario.items():
        print("key: %a - value: %a" % (key, value))
    pass
# Punto de entrada de cualquien aplicación de python
if __name__ == "__main__":
    run()