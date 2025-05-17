import random

l=[]
l_2 = []
num  = int(input("Enter the number of elements in original list: "))

for i in range(0, num):
    a = random.randint(0, 10)
    l.append(a)
    
print("Original List: ",l)

for i in range(0,5):
    l_2.append(l[i])
    
    

print("Extracted first five elements: ",l_2)

l_rev=[]
for i in range(4,-1,-1):
    l_rev.append(l_2[i])
    
print("Reversed extracted elements: ",l_rev)
