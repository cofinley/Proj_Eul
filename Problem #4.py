'''multiply 1-999 by 1-999
    if product is palidrome, store numbers and palindrome product in dictionary
palidrome criteria
    #find numbers with even digits (probably 6 digits in this case)
    #test if string == reverse of string
    '''

dict, dict1 = {}, {}

def fill(dict, dict1):
    for i in xrange(100,1000):
        for j in xrange(100,1000):
            var = i*j
            if (len(str(var)) % 6 == 0):
                key = "%d x %d" % (i,j)
                dict[key] = var
            else: continue
    return sort(dict, dict1)

def sort(dict, dict1):
    for i in dict:
        if (str(dict[i]) == str(dict[i])[::-1]):
            dict1[i] = (dict[i])
    dict1 = sorted(dict1.values())
    print dict1[-1]

fill(dict, dict1)
