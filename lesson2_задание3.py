# Задание 3:
# 1. Создайте словарь из участников нашей группы, где ключом будет фамилия, а значением имя.
# 2. Выведите имя любого из участников.
# 3. Добавьте с словарю еще одного участника на свой вкус.
# 4*. Создайте переменную с фамилией одного из участников и выведите его имя, 
# используя для этого одновременно 2 переменные - словарь участников и только что объявленную переменную.

_dict = {"Maksimenko": "Eakaterina", "Moskalevich": "Karina", "Ivankova": "Anastasia", "Volkova": "Svetlana", 
"Svechnikov": "Victor", "Sokolova": "Eugenia", "Dmitrieva": "Anna", "Okhotnikov": "Vitaly", "Chepelova": "Anna"}
print (_dict ["Volkova"])

_dict.update ({"Volodin": "Aleksey"})
print (_dict)

LastName = "Chepelova"
print (_dict[LastName])
