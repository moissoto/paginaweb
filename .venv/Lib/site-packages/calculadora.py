def operacion (n1:int,n2:int,op:int):
    match int(op):
        case 1:
            return (n1+n2)
        case 2:
            return (n1-n2)
        case 3:
            return (n1*n2)
        case 4:
            return (n1/n2)
        case 5:
            return (n1%n2)