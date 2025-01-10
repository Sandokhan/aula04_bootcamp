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
# fruit_list : list = ["maça", "banana", "cereja"]
# fruit_dict : dict = {"maça" : .45, "banana" : .3, "cereja" : .65}
# total : float = 0

# for k, v in fruit_dict.items():
#     if k in fruit_list:
#         total = total + v

# print(total)

# Exercise 6
# email : list = ["harry@potter.uk", "curtis@jobling.com", "harry@potter.uk", "jason@bourne.uk", "james@gunn.dc.us", "richard@darkins.com", "curtis@jobling.com"]
# print(list(set(email)))

# Exercise 7
# ages : list = [10, 20, 30, 40, 50, 60, 12, 15, 18, 5, 6]
# print([age for age in ages if age >= 18])

# Exercise 8
# people : list = [
#     {"nome": "Alice", "idade": 30},
#     {"nome": "James", "idade": 25},
#     {"nome": "Carol", "idade": 20},
#     {"nome": "Ash", "idade": 30},
#     {"nome": "Bob", "idade": 32},
# ]
# people.sort(key=lambda people: people["nome"])

# print(people)

# Exercise 9
# numbers : list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(f"Average: {sum(numbers) / len(numbers)}")

# Exercise 10
# numbers : list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# even : list = [number for number in numbers if number % 2 == 0]
# odd : list = [number for number in numbers if number % 2 != 0]
# print(f"Even: {even}")
# print(f"Odd: {odd}")

# Exercise 11
# produtos = [
#     {"id": 1, "nome": "Teclado", "preço": 100},
#     {"id": 2, "nome": "Mouse", "preço": 80},
#     {"id": 3, "nome": "Monitor", "preço": 300}
# ]
# produtos[2]["preço"] = 450
# print(produtos)

# Exercise 12
# dicionario1 = {"a": 1, "b": 2}
# dicionario2 = {"c": 3, "d": 4}

# dicionario_fundido = {**dicionario1, **dicionario2}

# print(dicionario_fundido)

# Exercise 13
estoque : dict = {"Teclado": 10, "Mouse": 0, "Monitor": 3, "CPU": 0}
for key in estoque.keys():
    if estoque[key] == 0:
        pass
    else:
        print(f"Produto {key} com estoque.")

