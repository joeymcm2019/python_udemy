import pandas as pd

data = pd.read_csv("nato_phonetic_alphabet.csv")

phonetic_dict = data.set_index("letter")["code"].to_dict()

name = input("Enter a name: ")


def foo(name):
    return [phonetic_dict[c.upper()] for c in name]


print(phonetic_dict)

print(foo(name))
