# Input three test scores
score1 = int(input("Enter first score: "))
score2 = int(input("Enter second score: "))
score3 = int(input("Enter third score: "))

# Find the minimum score
min_score = min(score1, score2, score3)

# Calculate the average of the best two scores
average = (score1 + score2 + score3 - min_score) / 2

print("The average of the best two scores is:", average)
