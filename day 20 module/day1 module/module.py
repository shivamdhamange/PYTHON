#module is a pyhton file which contains functions,classess and variables
#which can be reused  in any python program
#types of module
'''
1 --- built in module (math,random,os)
2 ------ third party modules (pandas ,numpy,scikit-learn,pytorch)
3 ------- user defined module (custum modules)
'''
########################################################

'''
import math

print(f"square root of 16 is : {math.sqrt(16)}")
print(math.pi)
print(math.cos(0))
print(math.sin(0))
print(math.tan(0))'''


########################################################

'''from math import pi,sqrt

print(pi)
print(sqrt(16))
'''

########################################################

'''from math import pi as p,sqrt as s

print(p)
print(s(16))'''


########################################################
'''Random  module'''
########################################################

import random as r
print(r.randint(1,10))


#######################################################