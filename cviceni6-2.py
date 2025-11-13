import requests

def download_rates(url):
    response = requests.get(url, timeout=2)
    if not response.ok:
        return None

    rates = {}

    # Text odpovědi - rozdělíme podle \n (nikoli /n)
    data = response.text.split('\n')

    # Přeskočíme první dva řádky (datum a hlavička)
    for line in data[2:]:
        # Odstraníme prázdné řádky
        if not line.strip():
            continue

        fields = line.split('|')

        # Kontrola správného počtu položek
        if len(fields) < 5:
            continue

        # fields[3] = kód měny (např. "EUR"), fields[4] = kurz
        rates[fields[3]] = float(fields[4].replace(',', '.'))

    return rates


if __name__ == "__main__":
    listek = download_rates("https://www.cnb.cz/cs/financni_trhy/devizovy_trh/kurzy_devizoveho_trhu/denni_kurz.txt")
    print(listek)
