
def calc_tax(amount, tax_rate, age):

    if not isinstance(amount, (int, float)):
        raise TypeError("wrong type of amount values: int or float required.")
    if not amount >= 0:
        raise ValueError("amount value must be positive.")

    if not isinstance(tax_rate, float):
        raise TypeError("tax rate value must be float type.")
    if not 0 < tax_rate < 1:
        raise ValueError("tax_rate value must be between 0 and 1.")

    if not isinstance(age, int):
        raise TypeError("Age value must be integer type")
    if not age > 0:
        raise ValueError("Age vale must be positive")

    if age <= 18:
        return int(min(amount * tax_rate, 5000))
    elif age <= 65:
        return int(amount * tax_rate)
    else:
        return int(min(amount * tax_rate, 8000))
