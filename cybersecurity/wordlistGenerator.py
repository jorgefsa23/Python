import itertools

string = input("String a ser permutado:  ")
#permutação de entrada em x permutações, no caso definido como longitude da palavra:
resultado = itertools.permutations(string, len(string))

for i in resultado:
    print(''.join(i))