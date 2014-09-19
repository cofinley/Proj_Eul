import math
list = [2]

for num in range(3,200000,2):
    if all((num % i !=0) for i in range(3, (int(math.sqrt(num))+1),2)):
        list.append(num)
        if len(list) > 10000: break

print list[10000]
