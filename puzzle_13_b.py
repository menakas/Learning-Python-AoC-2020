import sys 


def chinese_remainder(n, a):
    sum = 0
    prod = reduce(lambda a, b: a*b, n)
    print prod
 
    for n_i, a_i in zip(n, a):
        p = prod / n_i
        #print p, prod, n_i
        sum += a_i * mul_inv(p, n_i) * p
    return sum % prod
 
 
def mul_inv(a, b):
    b0 = b
    x0, x1 = 0, 1
    #print "INV ..",a,b
    if b == 1: return 1
    while a > 1:
        q = a / b
        a, b = b, a%b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0: x1 += b0
    #print "INV",a,b,x1
    return x1
 
first = 0
for line in sys.stdin:
    line = line.strip()
    if first:
        buses = line.split(',')
    first = 1

n = []
a = []
for i in range(0,len(buses)):
    if buses[i] != 'x':
         print int(buses[i])-i,int(buses[i]) 
         a.append(int(buses[i])-i) #remainder list
         n.append(int(buses[i])) #divisor list


if __name__ == '__main__':
    print chinese_remainder(n, a)



