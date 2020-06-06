import math

        
print('Wprowadź dane do równania')
print('a = ')
a = int(input())
print('b = ')
b = int(input())
print('c = ')
c = int(input())


d = b**2 - 4*a*c

if d < 0:
    print('Delta mniejsza od zera, brak rozwiązań')
    exit()

d_sqrt = math.sqrt(d)
    
x1 = (-b - d_sqrt)/(2*a)
x2 = (-b + d_sqrt)/(2*a)

print('Rozwiązania to:', "x1=", x1, "oraz", "x2=", x2)

