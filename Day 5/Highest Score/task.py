student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86, 55, 91, 64, 89]
max_score = 0
for i in range(len(student_scores)):
    if student_scores[i] > max_score: # Iteration through the array
        max_score = student_scores[i]
print(max_score)
