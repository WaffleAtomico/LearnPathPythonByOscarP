#Aprendizaje: Revisar cuando es viable sortear strings
def longestCommonPrefix(strs):
        n = 0
        if len(strs) == 1:
            return strs[0]
        resp = strs[0][:n]
        
        for n in range(len(strs[0])+1):
            resp = strs[0][:n]
            for x in range(len(strs)):
                if resp != strs[x][:n]:
                    print("Menos 1")
                    return strs[0][:(n-1)]
        print("Final")
        return resp
            
        # for i in strs[0]:
        #     for j in strs:
        #         if i not in j:
        #             return resp
        #     resp += i
        # return resp
                    
 
# lista = ["flower","flow","flight"]
# lista = ["dog","racecar","car"]    
# lista = ["aa","ab"]  
# lista = [""]    
# lista = ["a"] 
lista = ["flower","flower","flower","flower"]

print("respuesta", longestCommonPrefix(lista))




'''
 def longestCommonPrefix(self, strs):
        list = sorted(strs)
        res = ""
        first, last = list[0], list[-1]
        for i in range(min(len(first), len(last))):
            if first[i] == last[i]:
                res += first[i]
            else:
                break
        return res
'''