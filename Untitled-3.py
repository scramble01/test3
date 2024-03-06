num = 25
sqrt = num ** (0.5)

def is_int(value):
    if value == round(value):
        print("число из под корня получается натуральным это "+str(sqrt)")
    else:
        print("такого корня не существует")

c=4
d=4.5
is_int(c)
is_int(d)
