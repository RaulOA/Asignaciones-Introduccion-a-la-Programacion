import os
os.system("cls")

# Usuario : admin
# Pin : 1234

saldo=0
pin="1234"
intentos=3
transacciones=[]

while intentos>0:
    usuario=input("******************************************* Escriba su Usuario: ")
    usuario=usuario.lower()
    if usuario==("admin"):
        while intentos>0:
            p=input("******************************************* Digite su Pin: ")
            intentos=intentos-1
            if p==pin:
                while True:
                    print("""Menu Principal:

        1: Consultar Saldo
        2: Depositar
        3: Retirar
        4: Transacciones
        5: Salir                
        """)
                    opcion=input("Digite una Opcion: ")
                    
                    if opcion=="1":
                        print("~~~~~~~~~~~ CONSULTA DE SALDO ~~~~~~~~~~~")
                        print("----------- Tiene un saldo de :",str(saldo),"-----------")
                    elif opcion=="2":
                        print("~~~~~~~~~~~ DEPOSITO ~~~~~~~~~~~")
                        while True:
                            deposito=input("Digite el monto que quiere depositar: ")
                            numero=deposito.isdigit()
                            if numero==True:
                                deposito=int(deposito)
                                saldo=(saldo+deposito)
                                transacciones.append(["Deposito:",deposito])
                                print("----------- Depositado Exitoso -----------")
                                print("----------- Monto depositado:",deposito,"-----------")
                                print("----------- Saldo en tu cueta:",saldo,"-----------")
                                break; 
                            else:
                                print("/////////// Monto Invalido ///////////")
                    elif opcion=="3":
                        print("~~~~~~~~~~~ RETIRO ~~~~~~~~~~~")
                        while True:
                            retiro=input("Ingrese el multiplo de mil que desea retirar: ")
                            numero=retiro.isdigit()
                            if numero==True and saldo >0:
                                retiro=int(retiro)
                                retiro=retiro*1000
                                restante=(saldo-retiro)
                                if restante >= 0:
                                    saldo=(saldo-retiro)
                                    transacciones.append(["Retiro:",retiro])
                                    print("----------- Retiro Exitoso -----------")
                                    print("----------- Monto Retirado:",retiro,"-----------")
                                    print("----------- Saldo en tu cueta:",saldo,"-----------")
                                    break; 
                                else:
                                    print("/////////// Saldo Insuficiente, Su saldo es de:",saldo,"///////////")
                            elif numero ==True and saldo <1:
                                print("/////////// No puede retirar, Su saldo es 0 ///////////")
                                break
                            else:
                                print("/////////// Monto Incorrecto ///////////")
                    elif opcion=="4":
                        print("~~~~~~~~~~~ TRANSACCIONES ~~~~~~~~~~~")
                        for clave,valor in transacciones:
                            print("~~~~",clave,valor,"~~~~")
                    elif opcion=="5":
                        print("~~~~~~~~~~~ SALIR ~~~~~~~~~~~")
                        print("""
                        *************************************************************************
                        *************************************************************************
                        *************************************************************************
                        ******** Gracias por utilizar el Cajero Automatico de Raul.INC **********
                        *************************************************************************
                        *************************************************************************
                        *************************************************************************
                        """)
                        exit()
                    else:
                        print("/////////// Opcion no Valida ///////////")
            else:
                print("/////////// Pin Incorrecto, Le quedan",intentos,"intentos ///////////")
    else:
            print("/////////// Usuario Incorrecto ///////////")

            
if intentos<=0:
    print("/////////// Sistema Bloqueado, Consulte con el Banco ///////////")