import sys
import csv

def nacti_csv(soubor):
    data = []
    fp = open(soubor)
    reader = csv.reader(fp)
    for row in reader:
        data.append(row)
    fp.close()
    return data


def spoj_data(data1, data2):
    print(data1)
    print(data2)

    header1 = data1[0]
    header2 = data2[0]
    header = list(dict.fromkeys(header1 + header2))
    header.update(header1)
    header.update(header2)
    print(header)


    # 2. Vytvoř slovník (mapu) pro rychlejší přístup k datům 1
    # Klíčem je hodnota z prvního sloupce. Hodnotou je zbytek řádku.
    # Přeskoč hlavičku (data1[1:])
    data1_map = {row[0]: row[1:] for row in data1[1:]}
    
    vysledna_data = [spojene_hlavicky]
    
    # 3. Proveď spojení
    # Procházej data2, přeskoč hlavičku (data2[1:])
    for radek2 in data2[1:]:
        klic = radek2[0]  # Spojovací klíč
        zbytek_radku2 = radek2[1:]
        
        # Zkontroluj, jestli klíč existuje v datech 1 (INNER JOIN)
        if klic in data1_map:
            zbytek_radku1 = data1_map[klic]
            
            # Spoj řádky: (klíč) + (zbytek_řádku1) + (zbytek_řádku2)
            novy_radek = [klic] + zbytek_radku1 + zbytek_radku2
            vysledna_data.append(novy_radek)
            
    return vysledna_data


def zapis_csv(soubor, data):
    with open(soubor, "w") as fp:
        writer = csv.writer(fp)
        writer.writerows(data)


if __name__ == "__main__":
    try:
        soubor1 = sys.argv[1]
        soubor2 = sys.argv[2]
        csv_data1 = nacti_csv(soubor1)
        csv_data2 = nacti_csv(soubor2)
        vysledna_data = spoj_data(csv_data1, csv_data2)
        print(vysledna_data)
        zapis_csv("vysledny_excel.csv", vysledna_data)
    except IndexError:
        print("Nebyly zadany soubory")
    except FileNotFoundError:
        print("Soubor neexistuje")