def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        cont = 0 #4
        # print(cont)
        i = 1
        while n-i >= 0:
            n -= i
            cont += 1
            i+= 1
        return cont
    


def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        set1 = list( set(list1)&set(list2) )

        values = []
        for x in set1:
            values.append( (list1.index(x)+list2.index(x), x) )
        resp = []
        print(min(values))
        minimo = min(values)[0]
        for x in values:
            if x[0] == minimo:
                resp.append(x[1])
        return resp



    