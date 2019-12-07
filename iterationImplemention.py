import numpy as np

# add some constant here

# set the precision
precision = 1e-6

# here is the iteration process
def IterationWay(  ):
    valueNew,  valueOld= 3, 4
    while( np.abs(valueNew - valueOld) > precision):
        valueOld ,valueNew = valueNew ,funToBeSolved(valueOld)
        
    return valueNew

# here is the function to be solved
def funToBeSolved( x ):
    return x / np.log(x ** 2)

print(IterationWay())