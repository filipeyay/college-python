import itertools

def calc_combinacoes(elementos):
    combinacoes = []
    for i in range(1, len(elementos) + 1):
        sub_combinacoes = itertools.combinations(elementos, i)
        combinacoes.extend(sub_combinacoes)
    return combinacoes

def main():
    input_data = [1, 2, 3]
    combinacoes = calc_combinacoes(input_data)
    print("Combinações intermediárias: ", combinacoes)

if __name__ == "__main__":
    main()

def calc_combinacoes(elementos):
    combinacoes = []
    for i in range(1, len(elementos) + 1):
        sub_combinacoes = itertools.combinations(elementos, i)
        combinacoes.extend(sub_combinacoes)
    return combinacoes

def main():
    input_data = [1, 2, 3]
    combinacoes = calc_combinacoes(input_data)
    print(combinacoes)

if __name__ == "__main__":
    main()