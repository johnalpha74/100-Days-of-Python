age = eval(input("Enter age: "))

if (age >= 1) and (age <= 18):
    print("Important Birthday")

if (age == 21) or (age == 50):
    print("Important Birthday")

elif not (age < 65):
    print("Important Birthday")

else:
    print("Sorry Important Birthday")