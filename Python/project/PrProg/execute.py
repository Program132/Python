def dire(value):
    value = value.replace('"', "")
    value = value.replace(')', "")
    value = value.replace('(', "")
    value = value.replace('print', "")
    return print(value)

def direVar(value):
    value = value.replace('"', "")
    value = value.replace(')', "")
    value = value.replace('(', "")
    value = value.replace('print', "")
    return print(value)

def variable(name, value):
    value = value.replace('"', "")
    return #print("Name : " + name + ", value : " + value)