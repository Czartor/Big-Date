print('Wprowadź liczbę:')
print('n = ')
n = int(input())
    
if (n==0):
    print(1)
    exit()
else:
    wprowadzona_liczba = 1
    for i in range(1, n+1):
        wprowadzona_liczba *= i

    print("silnia z", n, "wynosi", wprowadzona_liczba)
