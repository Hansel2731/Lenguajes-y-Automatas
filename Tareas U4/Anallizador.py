print("Analizador Lexico")
print("")
file = open("libro.txt")
Operadores = {
    '+':'Suma',
    '-':'resta',
    '/':'Division',
    '*':'Multiplicacion',
    '^':'Potencia',
    '>':'Mayor',
    '<':'Menor',
    '>=':'Mayor que',
    '<=':'Menor que',
    '||':'Uno u otro',
    '!':'Diferente de',
    '=':'Igual',
    '&':'Y tambien'
}
Palabras_Clave = {
    'mod':'Metodo',
    'Opera':'Lbreria',
    'in':'Importar',
    'imp':'Imprimir',
    'for':'Ciclo For',
    'if':'Condicional',
    'else':'Condicional con dos casos o mas',
    'while':'Ciclo while',
    'switch':'Condicional switch',
    'do':'Ciclo condicional',
    'case':'Condicional switch con dos casos o mas',
    'pi':'Valor de pi',
    'rad':'Radianes',
    'sen':'Seno',
    'cos':'Coseno',
    'tan':'Tangente'
}
Delimitadores = {
    '(':'Inicio de agrupador de sentencia',
    ')':'Fianl de agrupador de sentencia',
    '{':'Inicio de encapsulador de codigo',
    '}':'Final de encapsulador de codigo',
    '[':'Inicio de determinador de valores',
    ']':'Final de determinador de valores',
    ';':'Terminacion de lina de codigo'
}
Numeros = {
    '0':'Cero',
    '1':'Uno',
    '2':'Dos',
    '3':'Tres',
    '4':'Cuatro',
    '5':'Cinco',
    '6':'Seis',
    '7':'Siete',
    '8':'Ocho',
    '9':'Nueve'
}

Operadores_key = Operadores.keys()
Palabras_Clave_key = Palabras_Clave.keys()
Delimitadores_key = Delimitadores.keys()
Numeros_key = Numeros.keys()

a = file.read() #leer el archivo
count=0 #contador
program = a.split("\n")
for line in program:
    count = count + 1
    print("linia",count,"\n",line)

    ##para leer separamos los tokens
    tokens = line.split(' ')

    print("Los tokens son: ",tokens)

    print("linea",count,"Propiedades \n")
    for token in tokens:
        if token in Operadores_key:
            print("El operador es: ",Operadores[token])

        elif token in Palabras_Clave_key:
            print("La palabra clave es: ",Palabras_Clave[token])

        elif token in Delimitadores_key:
            print("El delimitador: ",Delimitadores[token])

        elif token in Numeros_key:
            print("El numero es: ",Numeros[token])


    
print("--------------------------------------")


