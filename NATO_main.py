import pandas

a = pandas.read_csv("nato_phonetic_alphabet.csv")

dict = {row.letter:row.code for (index, row) in a.iterrows()}

word = input("Enter a word: ").upper()

list1 = [dict[i] for i in word]

print(list1)
