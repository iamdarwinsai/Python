# https://www.geeksforgeeks.org/loops-in-python/ (learn from here)

'''
while True:
    print("im joey")

while loop runs till condition becomes false
'''


joey=1
while joey<10:
    print(joey)
    joey+=1 # joey=joey+1


'''
for loop

it can be used in lists,tuples,dict,set,strings
'''

for i in range(1,3):
    for j in range(1,11):
        print(i*j,end=" ")
    print()