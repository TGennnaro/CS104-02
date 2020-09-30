#Initialize variables
total = scoreCount = average = 0

#Accept the number of scores to average
numberOfScores = int(input("Please enter the number of scores you want to average: "))

#Add a loop to make this code repeat until scoreCount = numberOfScores
while scoreCount < numberOfScores:
    score = int(input("Please enter a score: "))
    total += score
    scoreCount += 1

#Print the computed average
average = total / numberOfScores
print("The average is: "+str(average))
