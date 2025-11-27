import sys
import requests



def download_url_and_get_all_hrefs(url):
    """
    Funkce stáhne URL zadanou v parametru pomocí requests.get(),
    zkontroluje, že response.status_code == 200,
    a pokud ano, najde ve staženém obsahu všechny výskyty <a href="...">
    a vrátí seznam nalezených URL. Funguje bez ohledu na pořadí atributů.
    """
    response = requests.get(url)
    if response.status_code != 200:
        raise Exception(f"Chybný status kód: {response.status_code}")

    html = response.text
    hrefs = []

    start = 0
    while True:
        # najdeme začátek <a
        start_tag = html.find('<a ', start)
        start_tag_self = html.find('<a/>', start)
        
        if start_tag == -1:
            break  # žádný další <a tag
        
        # najdeme konec tagu (>)
        end_tag = html.find('>', start_tag)
        if end_tag == -1:
            break  # neuzavřený tag

        # v rozsahu tagu hledáme href="
        tag_content = html[start_tag:end_tag]
        href_pos = tag_content.find('href="')
        
        if href_pos != -1:
            # posuneme se za href="
            start_quote = start_tag + href_pos + len('href="')
            
            # najdeme konec uvozovek
            end_quote = html.find('"', start_quote)
            if end_quote != -1:
                link = html[start_quote:end_quote]
                hrefs.append(link)

        # posuneme hledání dál
        start = end_tag + 1

    return hrefs



if __name__ == "__main__":
    try:
        url = sys.argv[1]
        odkazy = download_url_and_get_all_hrefs(url)
        for odkaz in odkazy:
            print(f'"{odkaz}"')
    except Exception as e:
        print(f"Program skončil chybou: {e}")