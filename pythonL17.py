def f(city):
    if city == "Dushanbe":
        print(city + " population is 1M")
    if city == "Khujand":
        print(city + " population is 700K")
    if city == "":
        print("You didn't write any city name.")

f("Dushanbe")
f("Khujand")
f("")