def calculate_discount(price, discount_percent):
    """Calcule le prix après remise si >= 20%, sinon renvoie le prix initial."""
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
        return final_price
    else:
        return price


# Programme principal
try:
    price = float(input("Entrez le prix d'origine de l'article (€) : "))
    discount_percent = float(input("Entrez le pourcentage de remise (%) : "))

    final_price = calculate_discount(price, discount_percent)

    if discount_percent >= 20:
        print(f"Le prix final après une remise de {discount_percent}% est : {final_price:.2f} €")
    else:
        print(f"Aucune remise appliquée. Le prix reste : {final_price:.2f} €")

except ValueError:
    print("Veuillez entrer des valeurs numériques valides.")
