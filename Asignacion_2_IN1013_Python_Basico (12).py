"""

    12.	Introducir una cadena de caracteres e indicar si es un palíndromo.
    Una palabra palíndroma es aquella que se lee igual adelante que atrás.

"""

word=input("Digite una palabra: ")
word=word.lower()
inverse=word[::-1]

if inverse in word:
    print("La palabra",word.title(),"ES un palindromo")
else:
    print("La palabra",word.title(),"NO es palindromo")