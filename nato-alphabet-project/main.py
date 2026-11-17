import pandas as pd

df = pd.read_csv("nato_phonetic_alphabet.csv")

phonetic_alphabet = {row.letter:row.code for index,row in df.iterrows()}

name = input("What is your name?: ")
name = name.upper()

code_words = [phonetic_alphabet[letter] for letter in name if letter in phonetic_alphabet.keys()]

print(code_words)