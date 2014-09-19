for i in xrange(1,500):
    for j in xrange(1,500):
        for k in xrange(1, 500):
            if ((((i**2)+(j**2)) == (k**2)) and (i+j+k == 1000)):
                print i, j, k, "product = %d" % (i*j*k)
            else: continue
