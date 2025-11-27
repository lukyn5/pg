import json
import sys

class Auto:
    def __init__(self, znacka, model, barva):
        self.znacka = znacka
        self.model = model
        self.barva = barva

    def __str__(self):
        return f"Auto: {self.znacka} / {self.model} / {self.barva}"
    
    @classmethod
    def parse(cls, jdata):
        data = json.loads(jdata)
        for value in ("znacka", "model", "barva"):
            if value not in data:
                raise ValueError(f'Missing {value} in data')
        return cls(data['znacka'], data['model'], data['barva'])
    

if __name__ == "__main__":

    jdata1 = '{"znacka": "bmw", "model": "x5", "barva": "modra"}'

    data = json.loads(jdata1)

    if 'znacka' not in data:
        print('Invalid data: missing "značka"')
        sys.exit(1)

    if 'model' not in data:
        print('Invalid data: missing "model"')
        sys.exit(1)

    if 'barva' not in data:
        print('Invalid data: missing "barva"')
        sys.exit(1)


    znacka = data['znacka']
    model = data['model']
    barva = data['barva']

    auto = Auto.parse(jdata1)


