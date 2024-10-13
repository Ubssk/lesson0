immutable_var = 1, "name", 0.759, True
print(immutable_var)
#immutable_var[0] = 20 # кортеж не поддерживает обращение к элементам
mutable_list = ["one", 2, 3.0]
print(mutable_list)
mutable_list.append(True)
print(mutable_list)
mutable_list.extend(["Modified"])
print(mutable_list)
mutable_list.remove(3.0)
print(mutable_list)
mutable_list[1] = "two"
print(mutable_list)