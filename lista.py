file = open("lista.txt", "a+")
add = True
print("Podaj studentów do wczytania:")
studenci = []
while(add):
    print("Imie:")
    imie = input()
    print("Nazwisko:")
    nazwisko = input()
    print("Grupa:")
    grupa = input()
    studenci.append((imie, nazwisko, grupa))
    print("Czy chcesz dodać kolejnego studenta? Wpisz tak/nie")
    d = input()
    if d == "nie":
        add = False
for s in studenci:
    student = ", ".join(s)
    file.write(student)
    file.write("\n")
file.close()    

    
