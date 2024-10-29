def addBinary2(a, b):
    numA = int(a,2)
    numB = int(b,2)
    resp =  str(bin(numA + numB))[2:]
    return resp
       
    
a = '11'
b = '1'
print(addBinary2(a,b))    