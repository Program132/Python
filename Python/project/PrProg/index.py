import error
import execute

file = open("program.pr", "r")

lines = file.readlines()

for line in lines:
    line = line.strip()

    args = line.split()

    ## Le print ##

    if args[0] == "print":
        for lignesAvant in lines:
            
            l = lignesAvant.split()

            if l[0] == "variable":
                if l[1] == args[1]: 
                    execute.direVar(l[3])
                else:
                    if len(args) == 2:
                        value = args[1]
                        execute.dire(value)
                    else:
                        error.syntaxe()

    ## Les variables ##

    elif args[0] == "variable":
        if len(args) == 1:
            error.varAsync()

        elif len(args) == 2:
            error.varAsync()

        else:
            if not args[3]:
                error.varAsync()
            else:
                name = args[1]
                value = args[3]
                execute.variable(name, value)
    else:
        error.found(False)