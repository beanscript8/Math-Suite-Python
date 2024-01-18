import math

def isfloat(num):
    try:
        float(num)
        return True
    except ValueError:
        return False

def getfloat(name):
    while True:
        value = input(f"Input your {name}: ")
        if isfloat(value):
            return float(value)
        else:
            print(f"Does not look like '{value}' is a number.")
            print(f"Please make sure that {name} is a number.")
            continue

print("Welcome to the Distance Formula Calculator.")

x1 = getfloat("x1")
y1 = getfloat("y1")
x2 = getfloat("x2")
y2 = getfloat("y2")


distance = math.sqrt((x2-x1)**2 + (y2-y1)**2)
print(f"The distance of the two points is {distance}.")
