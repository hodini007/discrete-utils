from itertools import *
r=range(1,10)
#print(list(iter(r)))

# next(i) -> .__next__()
#iter(r) -> .__iter__()

''' counter =count(10,5)
for _ in counter:
    if _ == 1000:
        break
    else :
        print(_) '''

'''def accum(n:list):
    print(list(accumulate(n)))  #much more memory efficient

accum([1,2,3,4,5])'''

def perm (n,size):
    print(list(permutations(n,size)))

perm("abc",2)