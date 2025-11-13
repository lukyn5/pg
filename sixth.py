import sys
import requests



def download_url_and_get_all_hrefs(url):
    """
    Funkce stáhne URL zadanou v parametru pomocí requests.get(),
    zkontroluje, že response.status_code == 200,
    a pokud ano, najde ve staženém obsahu všechny výskyty <a href="...">
    a vrátí seznam nalezených URL.
    """
    response = requests.get(url)
    if response.status_code != 200:
        raise Exception(f"Chybný status kód: {response.status_code}")

    html = response.text
    hrefs = []

    start = 0
    while True:
        # najdeme začátek <a href="
        start_link = html.find('<a href="', start)
        if start_link == -1:
            break  # žádný další odkaz

        # posuneme se za <a href="
        start_quote = start_link + len('<a href="')

        # najdeme konec uvozovek
        end_quote = html.find('"', start_quote)
        if end_quote == -1:
            break  # neuzavřený odkaz

        link = html[start_quote:end_quote]
        hrefs.append(link)

        # posuneme hledání dál
        start = end_quote + 1

    return hrefs



if __name__ == "__main__":
    try:
        url = sys.argv[1]
        odkazy = download_url_and_get_all_hrefs(url)
        for odkaz in odkazy:
            print(f'"{odkaz}"')
    except Exception as e:
        print(f"Program skončil chybou: {e}")