def calculate_discount(price, discount_percent):
    """Calcule le prix après remise si >= 20%, sinon renvoie le prix initial."""
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
        return final_price
    else:
        return price

