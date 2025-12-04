"""
def nejvetsi(seznam_cisel=None):
    if seznam_cisel is None:
        return None
    return max(seznam_cisel)

def test_nejvetsi():
    assert nejvetsi([1, 2, 3, 4, 5]) == 5
    assert nejvetsi([100, 50, 30, 10]) == 100
    assert nejvetsi() == None
"""
def prevod_c_na_f(stupne):
    stupne_f = (stupne * (9 / 5)) + 32
    return stupne_f


def test_prevod_c_na_f():
    assert prevod_c_na_f(100) == 212
    assert prevod_c_na_f(0) == 32


    if __name__ == "__main__":
        pass