# this is a project solely made for education purposes it creates a list of all possible combination inside a text in the same folder where the code is running ... you can use this for brute force attacking 
from itertools import permutations
import os 

cases = str(input("Give all the letters or numbers separated by space : ")).split(' ')

cases = set(cases)
if '' in cases :
     cases.remove('')



len1 = int(input("Give the lowest length of the password : "))
len2 = int(input("Give the highest length of the password : "))

with open('myfile.txt', 'w') as fp:
    for i in range (len1 , len2+1):
        print("Running Case " + str(i))
        values = list(permutations(cases , i))
        values = [''.join(value) for value in values]
        # print(values)
        for x in values :
            fp.write(x+"\n")


fp.close()
