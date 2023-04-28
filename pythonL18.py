print("Welcome to this game! 😃")

playing = input("Do you want to play this game? ")

if playing.lower() != "yes":
    quit()

print("lets play!")
score = 0

answer = input("What is the capital of Tajikistan? ")
if answer.lower() == "dushanbe":
    print("Answer is correct 😃")
    score += 1
else:
    print("Wrong answer 😂")

answer = input("What is the population of Tajikistan? ") 
if answer == "11M":
    print("Answer is correct 😃")
    score += 1
else:
    print("Wrong answer 😂")

answer = input("Is Tajikistan a beautiful country? ")
if answer == "yes":
    print("Answer is correct 😃")
    score += 1
else:
    print("Wrong answer 😂")

print("Your score is " + str(score) + " correct answers.")
print("Your percentage is " + str((score / 3) * 100))

input("Press enter to exit")