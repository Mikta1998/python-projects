import pandas as pd

df = pd.read_csv("nato_phonetic_alphabet.csv")

phonetic_alphabet = {row.letter:row.code for index,row in df.iterrows()}
code_words = []

while True:
    try:
        name = input("What is your name?: ").upper()

        for letter in name:
            code_words.append(phonetic_alphabet[letter])
        print(code_words)
        break

    except KeyError:
        print(f"Only letter from the english alphabet are allowed!")
        code_words = []
