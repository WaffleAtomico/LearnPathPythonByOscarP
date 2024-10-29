#Aprendizaje, a veces es mejor usar un diccionario, que un if con distintas opciones, para evitar comparacion

def isValid(s):

        if s.count(')') ==  s.count('(') and s.count('{') ==  s.count('}') and s.count('[') ==  s.count(']'):
            #falta verificar el orden, antes de verificar si es true, debemos revisar que tenga orden, pero ya un avance es que tengan la misma cantidad
            pila = []
            for x in s:
                if x == '(' or x == '[' or x == '{':
                    print("Pila: ", pila, " Agregar: ", x)
                    pila.append(x)
                elif len(pila)>0:
                    print("Pila ", pila, " Quitar ", pila[-1], " x: ", x )
                    if (pila[-1] == '(' and x == ')') or (pila[-1] == '[' and x == ']') or (pila[-1] == '{' and x == '}'):
                        print("Pila ", pila, " Quitar ", pila[-1] )
                        pila.pop()
            if len(pila) == 0:
                return True
            else:
                return False
        return False
    
s = "[()]"
s = "[(])"
s = "(){}}{"
print(isValid(s))


'''
parent_stack = {')':'(','}':'{',']':'['}
        stack = []
        for char in s:
            if char in parent_stack:
                if stack and stack[-1] == parent_stack[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)
        return not stack   
'''