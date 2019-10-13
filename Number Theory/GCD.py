# Implementation of a recursive Euclidean algorithm and an extended Euclidean algorithm
def Euclidean(m,n):
    if m%n == 0:
        return n
    else:
        return Euclidean(n, m%n)

def Extended_Euclidean(m,n):
    x, px = 0, 1
    y, py = 1, 0

    while(n!=0):
        c = m%n
        d = int(m/n)
        
        m = n
        n = c

        temp = x
        x = px - d*x
        px = temp

        temp = y
        y = py - d*y
        py = temp
    # return m // this is the greatest common divisor of m ans n
    return px, py

a = int(input("Enter number a: "))
b = int(input("Enter number b: "))

x, y = Extended_Euclidean(a,b)

print("GCD of numebers {0} and {1} is equal: {2}".format(a, b, Euclidean(a,b) ))
print("Extended GCD: {0} = ({1}) * {2} + ({3}) * {4}  ".format(Euclidean(a,b), x, a, y, b))