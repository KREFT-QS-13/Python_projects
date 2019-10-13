def Euclidean(m,n):
    if m%n == 0:
        return n
    else:
        return Euclidean(n, m%n)

def Euler_function(x):
    result = 0
    for i in range(1,x):
        if Euclidean(i,n) == 1:
            result += 1
    return result

n = int(input("Enter number n: "))
print("The value of Euler function for n is equal: {}.".format(Euler_function(n))) 
