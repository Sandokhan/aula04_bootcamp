# Exercise 1
# square_list : list = [x**2 for x in range(11)]
# print(square_list)

# Exercise 2
# language_list : list = ["Python", "Java", "JavaScript", "C++"]
# print(language_list)
# print("Removing C++...")
# language_list.remove("C++")
# print("Adding Ruby...")
# language_list.append("Ruby")
# print("Final list")
# print(language_list)

# Exercise 3
# bookshelf : dict = {'Title' : 'SPQR', 'Author' : 'Mary Beard', 'Year' : 2015}
# for key, value in bookshelf.items():
#     print(f"{key}: {value}")

# Exercise 4
# word : str = "the fox jumps over the lazy dog"

# def count_letters(word: str) -> dict:
#     return {letter : word.count(letter) for letter in word}

# print(count_letters(word))

# Exercise 5
fruit_list : list = ["maça", "banana", "cereja"]
fruit_dict : dict = {"maça" : .45, "banana" : .3, "cereja" : .65}
total : float = 0

for k, v in fruit_dict.items():
    if k in fruit_list:
        total = total + v

print(total)