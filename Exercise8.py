print("Podaj słowo: ")
wpisane_słowo = input()
wpisane_słowo_as_list = list(wpisane_słowo)

for i in range(len(wpisane_słowo_as_list)):
    as_number = ord(wpisane_słowo_as_list[i])+1
    as_char = chr(as_number)
    wpisane_słowo_as_list[i] = as_char
    
wpisane_słowo_rotated = "".join(wpisane_słowo_as_list)
print(wpisane_słowo_rotated)
