import pandas

# Pandas used to turn csv into dataframe
data = pandas.read_csv('nato_phonetic_alphabet.csv')

# Creating a new dictionary by looping through df using dictionary comprehension & pandas
new_dict = {row.letter: row.code for (index, row) in data.iterrows()}


word = input("Enter a word: ").upper()
output_list = [new_dict[letter] for letter in word]
print(output_list)