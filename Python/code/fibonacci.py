a, b = (1, 1)
while b < 10:
    print 'a={0}, b={1} and a+b={2}'.format(a, b, (a+b))
    a, b = (b, a + b)