# Group members for this exercise are Daniel Cisneros, 
# Dene Logan, Ricky Sequera, and Joseph Onghena.

# This program executes the fibonacci sequence using recursion, as well
# as keeping track of the time that it takes to execute the given number.
# This code was inspired from https://www.geeksforgeeks.org/python-program-for-program-for-fibonacci-numbers-2/

import time 

start = time.time() # start timer

def fibo(num):
    if num == 0: # seed values
        return 0
    elif num == 1 or num == 2:
        return 1
    else:
        return fibo(num-1) + fibo(num-2) # recursive process of fibonacci sequence

result = fibo(35)
print(result)

end = time.time() # end timer

print('The program took ' + str(end-start) + ' seconds to execute.')