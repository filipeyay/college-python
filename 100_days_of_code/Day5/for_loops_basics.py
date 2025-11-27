fruits = ["Apple", "Peach", "Pear"]

# is going to loop assining the variable fruit to the value of each item of the list fruits

for fruit in fruits:
    print(fruit)
    print(fruit + " pie")

# ----------------------------------------------------------------------------------------#
student_score = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89]

total_exam_score = sum(student_score)
print(total_exam_score)

# creating the same example with for loop
sum = 0
for score in student_score:
    sum += score
print(sum)
