student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86]

print(max(student_scores))

max = 0
for score in student_scores:
    if score > max:  # is going to assign in order the values to score
        max = score  # if the next value is not greater then the last on it will ignore until the list ends

print(max)
