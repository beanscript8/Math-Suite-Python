import math

def isfloat(num):
    try:
        float(num)
        return True
    except ValueError:
        return False

print("Welcome to The Pythagorean Theorem Calculator.")
def getfloat(name):
    while True:
        val = input(f"Please input your {name}:")
        if isfloat(val):
            return float(val)
        else:
            print(f"Does not look like '{val}' is a number.")
            print(f"Please input {name} as a number value.")
            continue

aval = getfloat("a-value")
bval = getfloat("b-value")

cval= math.sqrt(aval ** 2 + bval ** 2)
print(f"The c value of your triangle is {cval}.")
