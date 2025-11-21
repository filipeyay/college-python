test_score = []

counter = 1

while counter <= 5:
    student_number = input("Nº: ")
    test_score = float(input("Score: "))
    result = [student_number, test_score]
    test_score.append(result)

    counter = counter + 1

print("Number of Test Scores: ", len(test_score))
