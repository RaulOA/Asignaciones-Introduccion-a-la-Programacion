"""

    9.	Realizar un sistema utilizando el lenguaje Python que solicite dos palabras
    y diga si riman o no. Si coinciden las tres últimas letras tiene que decir que riman.
    Si coinciden sólo las dos últimas tiene que decir que riman un poco y si no, que no riman.

"""

word1=input("Digite una palabra:    ")
word2=input("Digite otra palabra:   ")

if word1[:-4:-1] in word2[:-4:-1] or word1[:-3:-1] in word2[:-3:-1]:
    if word1[:-4:-1] in word2[:-4:-1]:
        print("Sus palabras riman")
    elif word1[:-3:-1] in word2[:-3:-1]:
        print ("Sus palabras riman un poco")
else:
    print("Sus palabras no riman")