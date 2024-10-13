# 2. Работа со словарями

my_dict = {'Имя(str)' : "Anna", 'Год рождения(int)' : 1990}
print("Dict:", my_dict)
print("Existing value:", my_dict.get('Имя(str)'))
print("Not existing value:", my_dict.get('Имя'))
my_dict.update({'Имя' : "Ivan", 'Год рождения' : 1995,})
print(my_dict)
a = my_dict.pop('Имя')
print("Deleted value:", a)
print("Modified dictionary:", my_dict)

# 3. Работа с множествами

my_set = {1, 2, 3, 4, 1, 4, 3.0, 5.7, 8.6, 5.7, "name", "date", "name", True, True, False, True, False}
print("Set: ", my_set)
my_set.add(9)
my_set.add("water")
my_set.discard(5.7)
print("Modified set: ", my_set)