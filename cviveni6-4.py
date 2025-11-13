from cviceni6_3 import download_rates
import sys

def currencies_amount(amount_czk, rates):
    """
    Převod z CZK na všechny měny podle kurzovního lístku ČNB.
    rates = {'AUD': (1, 13.690), 'EUR': (1, 24.230), ...}
    """
    conversions = {}

    for code, (amount, rate) in rates.items():
        # Přepočet: kolik jednotek cizí měny odpovídá dané částce v CZK
        conversions[code] = round(amount_czk * amount / rate, 2)

    return conversions


if __name__ == "__main__":

    if len(sys.argv) < 2:
        sys.exit("Zadej částku v CZK jako argument")

    amount = int(sys.argv[1])

    date, rates = download_rates(
        'http://www.cnb.cz/cs/financni_trhy/devizovy_trh/kurzy_devizoveho_trhu/denni_kurz.txt'
    )

    conversions = currencies_amount(amount, rates)

    print(f"Kurzy ze dne: {date}")
    for code, value in conversions.items():
        print(f"{code}: {value}")
