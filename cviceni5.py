import sys


def precti_hodnoty_a_incrementuj(file):

    all_results = []
    for line in file:
        data = line.split(',')
        result = []
        for value in data:
            value = value.strip().strip('"')
            try:
                value = int(value) + 1
            except ValueError:
                pass
            result.append(value)
        all_results.append(result)
    return all_results


def zapis_data_do_csv(file_name, data):

    with open(file_name, "w") as file:
        for row in data:
            row2 = []
            for value in row:
                row2.append(str(value))
            line = ','.join(row2)
            file.write(line + '\n')

    pass


def precti_hodnoty_a_incrementuj2(file):
    data = []
    reader = csv.reader(file)
    for row in reader:
        line = []
        for value in row:
            try:
                value = int(value)

            except ValueError:
                pass
            line.append(value)
        data.append(line)
    return data

def zapis_data_do_csv2(file_name, data):
    with open(file_name, "w") as file:
        writer = csv.writer(file)
        writer.writerows(data)


def spoj_data(data1, data2):
    



if __name__ == "__main__":

    try:
        name = input("Zadej jmeno souboru: ")
        file = open(name, "r")
        results = precti_hodnoty_a_incrementuj(file)
        file.close()
        name, ext = name.split('.')
        file_name = name + '2.' + ext #zapiš hodnoty z result do data2.txt
        zapis_data_do_csv(file_name, results)
    except FileNotFoundError:
        print(f'Soubor {name} neexistuje')