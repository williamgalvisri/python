def run():
    for contador in range(1000):
        if contador % 2 != 0:
            continue
        print(contador)

# Punto de entrada de cualquien aplicación de python
if __name__ == "__main__":
    run()