
def is_int(value):
    if value == round(value):
        print("число из под корня получается натуральным")
    else:
        print("такого корня не существует")

c=4
d=4.5
is_int(c)
is_int(d)
