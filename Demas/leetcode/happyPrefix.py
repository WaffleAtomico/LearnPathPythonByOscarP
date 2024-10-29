#TAREA: COMPRENDER Y HACERLO MAS EFICIENTE
def happyprefix(s):
    for x in range(len(s)):
        print(s[x:])
        print(s[:-x])
        if s[x:] == s[:-x]:
            return s[x:]
    return ""
    
frase = "level"
# frase = "ababab"

print(happyprefix(frase))