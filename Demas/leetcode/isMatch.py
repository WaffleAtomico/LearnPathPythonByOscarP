def isMatch(s, p):
        puntos_s =  s.count('.')
        asterisco_s = s.count('*')
        puntos_p = p.count('.')
        asterisco_p = p.count('*')
        if puntos_s == 0 and asterisco_s == 0 and puntos_p ==0 and asterisco_p ==0:
            return s == p
        
        # Si hay un caracter ASCII, que no haya en el otro, lo eliminamos
        # buscamos que si quepa en
        # print(' '.join(s.replace('*', '').replace('.', '')).split())
        # print(' '.join(p.replace('*', '').replace('.', '')).split())
        comunes = set(' '.join(s.replace('*', '').replace('.', '')).split()) & set(' '.join(p.replace('*', '').replace('.', '')).split())
        comunes = list(comunes)
        # print("Comunes ",comunes)
        
        cola_s = []
        for x in s: #el primero que si exista en ambas sera nuestro pivote
            if x in comunes:
                cola_s.append(x) 
                break 
            
        if len(cola_s) == 0:
            cola_s.append(s[0]) 
            
        # prev = None
        for x in s:
            aux = x
            if aux == '*':
                if cola_s[-1] not in comunes:
                    cola_s.pop()
            if aux != cola_s[-1] and aux != '.' and aux != '*':
                # print(f"Existe? {aux} {comunes}", aux in comunes)
                # if aux in comunes:
                    cola_s.append(aux)
            # prev = aux
            
        cola_p = []
        for x in p: #el primero que si exista en ambas sera nuestro pivote
            if x in comunes:
                cola_p.append(x) 
                break      
        if len(cola_p) == 0:
            print("Cola P se queda vacia")
            cola_p.append(p[0])
            
        # prev = None
        for x in p:
            aux = x
            if aux == '*':
                if cola_p[-1] not in comunes:
                    cola_p.pop()
                    
            if aux != cola_p[-1] and aux != '.' and aux != '*':
                # print(f"Existe? {aux} {comunes}", aux in comunes)
                # if aux in comunes:
                    cola_p.append(aux)
                    
        # print("ColaS",cola_s)
        # print("ColaP",cola_p)
        if len(cola_s) != len(cola_p):
            return False
        for x, y in zip(cola_s, cola_p):
            if x != y: #x != '.' or y != '.' or
                print(x,y)
                if x == '.' or y == '.':
                    continue
                return False
        return True

s = 'ab' #"abcd" #"aab"
p = '.*' #"d*" #"c*a*b"
print(isMatch(s,p))