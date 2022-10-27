from fractions import Fraction

def iterator(n):
    return [Fraction(1,2**n+k) for k in range(1,2**n+1)]  

def iterator2(n):
    return [(1,2**n) for k in range(1,2**n+1)] 

print([sum(iterator(i)) > Fraction(1, 2)for i in range(1,15)])
# print([[iterator2(i)] for i in range(1,5)])