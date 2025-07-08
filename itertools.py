# from itertools import product
# a = [1,2,8]
# b= [3]
# prod = product(a,b,repeat=2)
# print(list(prod))

from itertools import accumulate
import operator
a = [1, 2, 3, 4]
print(a)
acc = accumulate(a, func=operator.mul)
print(list(acc))