print('Wprowadź liczbę:')
print('n = ')
n = int(input())
    
if (n==0):
    print(1)
    exit()
else:
    factorial = 1
    for i in range(1, n+1):
        factorial *= i

    print("silnia z", n, "wynosi", factorial)
