discount = {1000: 0.03, 5000:0.05, 7000:0.07, 10000:0.1, 50000:0.15}
tax = {"UT": 0.0685, "NV": 0.008, "TX": 0.0625, "AL": 0.04, "CA": 0.0825}

def get_discount(value):
    if value >= 50000:
        return 0.15
    if value >= 10000:
        return 0.1
    if value >= 7000:
        return 0.07
    if value >= 5000:
        return 0.05
    if value >= 1000:
        return 0.03
    return 0


def main():
    nb_art = int(input("nombre d'article : "))
    pu = float(input("prix par article : "))

    total = nb_art * pu
    print(f"total HT {total}€")

    cp = input("code postal : ")
    montant_tax = tax[cp]
    calc_tax = total * montant_tax
    prix_ttc = total + calc_tax
    print(f"prix TTC : {prix_ttc}€")

    reduce_taux = get_discount(prix_ttc)
    print(f"your reduce taux is {reduce_taux}")
    reduction = prix_ttc * reduce_taux
    print(f"your reduction discount is {reduction}€")


    print(f"Your total after discount : {prix_ttc-reduction}€")

main()