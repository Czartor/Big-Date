file = open("dna.txt", "r")
dna = file.read()
count_of_C = dna.count('C')
count_of_G = dna.count('G')
x = (count_of_C+count_of_G)/len(dna)
print("C+G stanowi ", x * 100, "%")
