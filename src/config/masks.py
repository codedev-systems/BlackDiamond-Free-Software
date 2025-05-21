#Máscara Monetária
def monetaryMask(value):
    return f"R${value:,.2f}".replace(",", "x").replace(".", ",").replace("x", ".").replace("-", "")