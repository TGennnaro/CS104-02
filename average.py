#Initialize variables
total = scoreCount = 0
average = 0.0

#Accept the number of scores to average
numberOfScores = int(input("Please enter the number of scores you want to average: "))

#Add a loop to make this code repeat until scoreCount = numberOfScores
score = int(input("Please enter a score: "))
total += score
scoreCount += 1


average = total / numberOfScores
print(average)
