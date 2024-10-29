def plusOne(digits):
        resp = ""
        for x in digits:
            resp += "".join(str(x))
        # print("1: ", resp)
        resp = int(resp)
        # print("2: ", resp)
        resp += 1
        # print("3: ", resp)
        resp = " ".join(str(resp))
        
        # print("4: ", resp)
        # print("final: ", resp.split())
        resp = resp.split()
        resp = list(map(int,resp))
        return resp
    
    
lista = [1,2,3]
print(plusOne(lista))