var = 2

for num in xrange(3,2000000,2):
    if all((num % i !=0) for i in xrange(3, (int(num**0.5)+1), 2)):
        var += num
