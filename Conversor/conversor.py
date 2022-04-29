# Nota funciones predeterminadas de python se llaman "built in"
def convertCurrency(tc):
    pesos = input("¿Cuantos dolares tienes?: ");
    pesos = float(pesos);
    print(tc);

    valor_dolar = tc;

    dolares = round(pesos * valor_dolar, 2);
    # Pintar el valor
    print("Tienes $"+str(dolares)+" dolares");


nombre = input("Hola, ¿Cual es tu nombre?").capitalize();
menu = """
    %s, Bienvenido al conversor de dolares a

    1 - Pesos colombianos
    2 - Pesos argentinos
    3 - Pesos Mexicanos

    elije una opción:
""" % (nombre);
1
opcion = int(input(menu))
currencyValue = 0;
if opcion == 1: 
    currencyValue = 3875;
elif opcion == 2:
    currencyValue = 37.74;
elif opcion == 3:
    currencyValue = 20.31;
else:
    print("Opción incorrecta");

convertCurrency(currencyValue);





