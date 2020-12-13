with open("prog.txt", "r") as file:
    lines = file.readlines()
    file.close

    def Syntaxe():
        return print("SYNTAXE INVALIDE")

    def variable(name, value):
        mavar = value
        return mavar #print("variable " + name + " = " + value)

    def direPrint(value):
        return print(value)

    def PrintWithVar(value):
        return print(value)

    for line in lines:
        line = line.strip()

        args = line.split()
        
        if args[0] == "variable":
            if len(args) == 1:
                Syntaxe()
            elif len(args) == 2:
                Syntaxe()
            else:
                if args[2] == "=":
                    variable(args[1], args[3])

        elif args[0] == "print":
            if len(args) == 1:
                Syntaxe()
            else:
                direPrint(args[1]) #print(args[1])

        elif args[0] == "BeyProg":
            print("Commande de Test du langage")