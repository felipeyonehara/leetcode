def calPoints(ops) -> int:
    
    result = 0
    lista = list()
    last_index = 0
    print(ops)
    for i in range(len(ops)):
        if( ops[i] == "+"): 
            # print("+")
            lista.append(int(lista.__getitem__(last_index-1)) + int(lista.__getitem__(last_index-2)))
            last_index=last_index + 1
            # print(result)
        if( ops[i] == "D"): 
            # print("D",last_index)
            # value = ops[last_index]
            lista.append(int(lista.__getitem__(last_index-1))*2)
            last_index = last_index+1
        if( ops[i] == "C"): 
            lista.pop()
            last_index = last_index - 1
        if( ops[i].isnumeric() or ops[i][0] == '-'):
            lista.append(int(ops[i]))
            last_index = last_index + 1
        # print("lista:",lista)
        
    
    for i in lista:
        result = result + i
    
    # print(result,lista)
    return result

print(calPoints(["5","-2","4","C","D","9","+","+"]))