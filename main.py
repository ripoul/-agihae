discount = {1000: 0.03, 5000:0.05, 7000:0.07, 10000:0.1, 50000:0.15}
tax = {"UT": 0.0685, "NV": 0.008, "TX": 0.0625, "AL": 0.04, "CA": 0.0825}


def main():
    nb_art = int(input("nombre d'article : "))
    pu = int(input("prix par article : "))

    total = nb_art * pu
    print(f"total HT {total}€")

    cp = input("code postal : ")
    montant_tax = tax[cp]
    calc_tax = total * montant_tax
    prix_ttc = total + calc_tax
    print(f"prix TTC : {prix_ttc}€")

main()