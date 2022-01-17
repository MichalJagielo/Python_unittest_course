
def calc_tax(amount, tax_rate):

    if not isinstance(amount, (int, float)):
        raise TypeError("wrong type of amount values: int or float required.")
    if not amount >= 0:
        raise ValueError("amount value must be positive.")

    if not isinstance(tax_rate, float):
        raise TypeError("tax rate value must be float type.")
    if not 0 < tax_rate < 1:
        raise ValueError("tax_rate value must be between 0 and 1.")

    return amount * tax_rate



