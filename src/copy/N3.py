
# Bibliotecas importadas
import itertools

# Célula 1: Entrada de Dados

# Função para calcular as combinações intermediárias
def calculate_combinations(elements):
    combinations = []
    for i in range(1, len(elements) + 1):
        sub_combinations = itertools.combinations(elements, i)
        combinations.extend(sub_combinations)
    return combinations

# Função principal
def main():
    input_data = [1, 2, 3]
    combinations = calculate_combinations(input_data)
    print("Combinações intermediárias:", combinations)

if __name__ == "__main__":
    main()

# Célula 2: Cálculos Intermediários
def calculate_combinations(elements):
    combinations = []
    for i in range(1, len(elements) + 1):
        sub_combinations = itertools.combinations(elements, i)
        combinations.extend(sub_combinations)
    return combinations

# Célula 3: Apresentação dos Resultados
def main():
    input_data = [1, 2, 3]
    combinations = calculate_combinations(input_data)
    print(combinations)

if __name__ == "__main__":
    main()
