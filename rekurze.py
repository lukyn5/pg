def faktorial(n):
    #fce vypocita faktorial
    # 0! -> 1
    # 5! -> 120

    if n == 0 or n == 1:
        return 1

    return n * faktorial(n - 1) # např. 10 * 9 

def faktorial2(n):
    result = 1
    #spocita fakt. pomocí fcyklu
    if n == 0:
        return 1
    for i in range(1, n + 1):
        result *= i
    return result




if __name__ == "__main__":


    print(faktorial2(0))
    print(faktorial2(1))
    print(faktorial2(5))
    print(faktorial2(100))