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

print("Welcome to the Quadratic Formula Calculator.")

bval = b.getfloat("b value")
aval = a.getfloat("a value")
cval = c.getfloat("c value")
squarerootpart = math.sqrt((b**2-*(4*a*c)/(2*a)) 
