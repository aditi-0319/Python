import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
new_data = pandas.DataFrame(data)

data_dict = {row.letter: row.code for (letter, row) in new_data.iterrows()}


def correct_answer():
    ans = input("Enter a word : ").upper()
    word = [n for n in ans]
    try:
        nato_list = [data_dict[nato] for nato in word if nato in data_dict[nato]]
    except KeyError:
        print("Invalid entry. You can input alphabets only.\n")
        correct_answer()
    else:
        print(f"NATO Phonetic Alphabet : {nato_list}")


correct_answer()
