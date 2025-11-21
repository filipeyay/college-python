import itertools


def calc_combinations(elements):
    combinations = []
    for i in range(1, len(elements) + 1):
        sub_combinations = itertools.combinations
        (elements, i)
        combinations.extend(sub_combinations)
    return combinations


def main():
    input_data = [1, 2, 3]
    combinations = calc_combinations(input_data)
    print("Intermediate Combinations: ", combinations)


if __name__ == "__main__":
    main()
