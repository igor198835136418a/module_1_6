my_dict = {"Рыська":2010, "Симба":2018}
print(my_dict)
print(my_dict.get("Рыська"))
print(my_dict.get("Set"))
my_dict.update({"Alisa":2000, "Melisa":2001})
a = my_dict.pop("Рыська")
print(a)
print(my_dict)

my_set = {1, 1, 2, 2,"Alisa", 3, 3, 4, 4, 5, 5}
print(my_set)
my_set.add(10)
my_set.add(20)
print(my_set)
my_set.discard(2)
print(my_set)


