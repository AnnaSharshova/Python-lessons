# Задание: 
# Задан список: furniture = ["chair", "table", "wardrobe", "sofa", "bed"]

# 1. Вывести все элементы этого списка, используя цикл.
# 2. В цикле вывести название каждого предмета мебели, кроме дивана. 
# 3. Расширить список furniture 2-мя новыми предметами мебели не создавая новый список. Вывести все элементы расширенного списка.
# 4. В цикле, если мы встречаем стол, то вывести "на нем можно писать", если встретим стул, то вывести "на не можно сидеть". Других выводов быть не должно.

furniture_list = ["chair", "table", "wardrobe", "sofa", "bed"]

for furniture_item in furniture_list:
    print(furniture_item)

no_sofa = [furniture_item for furniture_item in furniture_list if furniture_item != "sofa"]
print(no_sofa)

furniture_list.append("armchair")
furniture_list.append("coffee_table")
print(furniture_list)

for furniture_item in furniture_list:
    if furniture_item == "table":
        print("You can write on it")
    if furniture_item == "chair":
        print("You can sit on it")
