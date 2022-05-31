from pets import Cat, Dog

cat1 = Cat('Skif', 'boy', 1.5)

print("cat1.name = ", cat1.name)
print("cat1.gender = ", cat1.gender)
print("cat1.age = ", cat1.age)
print()
print("get_name = ", cat1.get_name())
print("get_gender = ", cat1.get_gender())
print("get_age = ", cat1.get_age())
print()

sam = Dog('Sam', 'boy', 2)
print(sam.get_pet())