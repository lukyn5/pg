"""
def my_range(start, stop, step=1):
    result = []
    actual = start

    while actual < stop:
        result.append(actual)
        actual += step
    return result

def while_enumerate(iterable, start=0):
    result = []
    index = 0 # index prvku na který ukazujeme


    while index < len(iterable):
        result.append( (start + index , iterable[index]))
        index += 1

     return result

"""

"""
def for_enumerate(iterable, start=0):
    result = []
    index = 0 # index prvku na který ukazujeme

    for el in iterable:
        result.append((start + index , el))
        index += 1
        
    return result
"""

#rekurze



    








if __name__ == "__main__":

    #text = "abcdef"
    #print(list(enumerate(text, 100)))
    #print(for_enumerate(text, 100))

    #print(text[3])

   # print(my_range(1, 7, 2))


    