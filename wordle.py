import sys

def check_in_array(check, ref, exclude):
    printable = False
    for i,element in enumerate(check[0:5]):
        if element.upper() == ref[i].upper():
            printable = True
        if element.upper() in exclude.upper():
            printable = False
    
    if printable: return printable

if len(sys.argv) != 7:
    print("Usage: wordle.py letter letter letter letter letter exclutionletters")
    sys.exit(0)

ref_word = []

alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
exclude = sys.argv[6]

for arg in sys.argv[1:6]:
    if arg == '?':
        ref_word.append("")
    if arg.upper() in alpha:
        ref_word.append(arg.upper())

with open('new_dict.txt','r') as file: 
    wordle_dict = file.readlines()


for word in wordle_dict:
    if check_in_array(word, ref_word, exclude):
        print("Found:" + word)
