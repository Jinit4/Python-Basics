pets = "Cats & Dogs"
print(pets.index ("s"))

def is_leap(year):
    leap=False
    if year%4 == 0 and year%100 != 0 or year%400 == 0:
        print("True")
    return leap

is_leap (2001)