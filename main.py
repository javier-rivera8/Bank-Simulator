def space(s):
    print("-----------------------")
space(1)
def eng(e):
    name = input("Name: ")
    balance = float(input("Enter starting balance: "))
    space(1)
    print("Account: " + name)
    print("Balance: " + "$" + str(balance))
    space(1)
    print("You may: ")
    #Menu----------------------------------
    print("1) Deposit some funds: ")
    print("2) Withdraw some funds: ")
    print("3) Quit")
    #Options--------------------------------
    select = input("Select: ")
    tax = 5
    taxi = 0
    deposits = 0
    withdraw = 0
    while select != "3":
        if select == "1":
            deposit = float(input("Deposit: "))
            balance = balance + deposit
            balance -= tax
            deposits += 1
            taxi += 1
            space(1)
            print("Account: " + name)
            print("New Balance: " + "$" + str(balance))
            space(1)
            print("You may: ")
            # Menu----------------------------------
            print("1) Deposit some funds: ")
            print("2) Withdraw some funds: ")
            print("3) Quit")
            select = input("Select: ")
        elif select == "2":
            out = float(input("Withdraw: "))
            if out > balance:
                space(1)
                print("Not enough funds")
                balance -= tax
                withdraw += 1
                taxi += 1
                space(1)
                print("Account: " + name)
                print("Balance: " + "$" + str(balance))
                space(1)
                print("You may: ")
                # Menu----------------------------------
                print("1) Deposit some funds: ")
                print("2) Withdraw some funds: ")
                print("3) Quit")
                select = input("Select: ")
                space(1)
            else:
                balance = balance - out
                balance -= tax
                withdraw += 1
                taxi += 1
                space(1)
                print("Account: " + name)
                print("Balance: " + "$" + str(balance))
                space(1)
                print("You may: ")
                # Menu----------------------------------
                print("1) Deposit some funds: ")
                print("2) Withdraw some funds: ")
                print("3) Quit")
                select = input("Select: ")
                space(1)
    space(1)
    print("Summary: ")
    print("Account: " + name)
    print("Deposits total:", deposits)
    print("Withdrawn total: ", withdraw)
    print("Tax total:" + "$" + str(tax*taxi))
    print("Balance: " + "$" + str(balance))
    print("Thank You!!")
def spa(s):
    name = input("Nombre: ")
    balance = float(input("Balance: "))
    space(1)
    print("Cuenta: " + name)
    print("Balance: " + "$" + str(balance))
    space(1)
    print("Opciones: ")
    #Menu----------------------------------
    print("1) Deposito: ")
    print("2) Retiro: ")
    print("3) Salir")
    #Options--------------------------------
    select = input("Seleccione: ")
    tax = 5
    taxi = 0
    deposits = 0
    withdraw = 0
    while select != "3":
        if select == "1":
            deposit = float(input("Depositar: "))
            balance = balance + deposit
            balance -= tax
            deposits += 1
            taxi += 1
            space(1)
            print("Cuenta: " + name)
            print("Nuevo balance: " + "$" + str(balance))
            space(1)
            print("Opciones: ")
            # Menu----------------------------------
            print("1) Deposito: ")
            print("2) Retiro: ")
            print("3) Salir")
            select = input("Seleccione: ")
        elif select == "2":
            out = float(input("Retirar: "))
            if out > balance:
                space(1)
                print("No hay fondos suficientes")
                balance -= tax
                withdraw += 1
                taxi += 1
                space(1)
                print("Cuenta: " + name)
                print("Balance: " + "$" + str(balance))
                space(1)
                print("Opciones: ")
                # Menu----------------------------------
                print("1) Depositar: ")
                print("2) Retirar: ")
                print("3) Salir")
                select = input("Seleccione: ")
                space(1)
            else:
                balance = balance - out
                balance -= tax
                withdraw += 1
                taxi += 1
                space(1)
                print("Cuenta: " + name)
                print("Balance: " + "$" + str(balance))
                space(1)
                print("Opciones: ")
                # Menu----------------------------------
                print("1) Depositar: ")
                print("2) Retirar: ")
                print("3) Salir")
                select = input("Seleccione: ")
                space(1)
    space(1)
    print("Resumen: ")
    print("Cuenta: " + name)
    print("Deposito total:", deposits)
    print("Retiro total: ", withdraw)
    print("Impuesto total:" + "$" + str(tax*taxi))
    print("Balance: " + "$" + str(balance))
    print("Gracias!!")
def fra(f):
    name = input("Nom: ")
    balance = float(input("Entrer le solde: "))
    space(1)
    print("Compte: " + name)
    print("Solde: " + "$" + str(balance))
    space(1)
    print("Vous pouvez: ")
    #Menu----------------------------------
    print("1) Deposer des fonds: ")
    print("2) Retirer certains fonds: ")
    print("3) Arreter")
    #Options--------------------------------
    select = input("Selectionner: ")
    tax = 5
    taxi = 0
    deposits = 0
    withdraw = 0
    while select != "3":
        if select == "1":
            deposit = float(input("Depot: "))
            balance = balance + deposit
            balance -= tax
            deposits += 1
            taxi += 1
            space(1)
            print("Compte: " + name)
            print("Nouveau solde: " + "$" + str(balance))
            space(1)
            print("Vous pouvez: ")
            # Menu----------------------------------
            print("1) Deposer des fonds: ")
            print("2) Retirer certains fonds: ")
            print("3) Arreter")
            select = input("Selectionner: ")
        elif select == "2":
            out = float(input("Retirer: "))
            if out > balance:
                space(1)
                print("Pas assez de fonds")
                balance -= tax
                withdraw += 1
                taxi += 1
                space(1)
                print("Compte: " + name)
                print("Solde: " + "$" + str(balance))
                space(1)
                print("Vous pouvez: ")
                # Menu----------------------------------
                print("1) Deposer des fonds: ")
                print("2) Retirer certains fonds: ")
                print("3) Arreter")
                select = input("Selectionner: ")
                space(1)
            else:
                balance = balance - out
                balance -= tax
                withdraw += 1
                taxi += 1
                space(1)
                print("Compte: " + name)
                print("Solde: " + "$" + str(balance))
                space(1)
                print("Vous pouvez: ")
                # Menu----------------------------------
                print("1) Deposer des fonds: ")
                print("2) Retirer certains fonds: ")
                print("3) Arreter")
                select = input("Selectionner: ")
                space(1)
    space(1)
    print("Resume: ")
    print("Compte: " + name)
    print("Total des depots:", deposits)
    print("Total retire: ", withdraw)
    print("Taxes total:" + "$" + str(tax*taxi))
    print("Solde: " + "$" + str(balance))
    print("Merci!!")
print("Welcome - Bienvenido - Benvenue")
space(1)
print("1) English")
print("2) Espanol")
print("3) Frances")
l = input("Language: ")
space(1)
if l == "1":
    eng(1)
elif l == "2":
    spa(1)
elif l == "3":
    fra(1)