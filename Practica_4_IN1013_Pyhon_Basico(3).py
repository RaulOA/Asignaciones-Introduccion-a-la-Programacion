"""3. Realizar un programa en python que cree una lista y esta la inicialízala con 5 cadenas
de caracteres leídas por teclado y estos deben de ser mostrados"""
import os
os.system("cls")

lista=[]

for i in range(5):
    lista.append(input("""Digite un Caracter: """))

for i in lista:
    print(i)