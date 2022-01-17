
# 1 Simple check values
"""
def total_price(net_price, tax_rate, discount=False):
    if not discount:
        return int(net_price * (1 + tax_rate / 100))
    else:
        return int(net_price * (1 + tax_rate / 100)* 0.9)

print(total_price(120, 45))
print(total_price(120, 45, True))
"""


# 1.1 Conditions
"""
condition = False  # True
if not condition:
     raise AssertionError("Assertion!")  # == assert condition, "Assertion!!!"
"""


# 1.2 Condition
"""
amount = 1000
tax_rate = .15
assert amount >= 0, "The amount must be grater than 0!"
assert 0 < tax_rate < 1, "The tax_rate must between 0 and 1"
"""


# 1.3 Condition
"""
def calc_area():

    width = float(input("Enter width of rectangle - ..."))
    height = float(input("Enter height of rectangle - ..."))

    if width < 0:
        raise ValueError("The width must be positive.")
    elif height < 0:
        raise ValueError("The height must be positive.")
    else:
        area = width * height

    return f"The Area of rectangle is: {area:.2f}"

print(calc_area())
"""


# 1.4 Condition
"""
def calc_area(a, b):
    return a * b

assert calc_area(4,44) == 16, "Enter correct values!"
"""