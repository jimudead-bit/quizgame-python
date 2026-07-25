score=0

print("Hello! Hope you are doing well")
print("\nWelcome to the quiz game! You will be asked 3 questions. Please answer using letters only.")
print("\nGood Luck!")

question1 = ("What is the necessary ingredient in finger fries?\na) Potatoes\nb) Tomatoes\nc) Onions","a")
answer = input(question1[0] + "\nYour answer: ").strip().lower()
if answer == question1[1]:
    print("Correct!")
    score += 1
else:
    print("Incorrect! The correct answer is a) Potatoes.")
print(f"Your current score is: {score}\n")

question2 = ("Which gas do humans need to breathe?\na) Nitrogen\nb)Carbon Dioxide\nc) Oxygen","c")
answer = input(question2[0] + "\nYour answer: ").strip().lower()
if answer == question2[1]:
    print("Correct!")
    score += 1
else:
    print("Incorrect! The correct answer is c) Oxygen.")
print(f"Your current score is: {score}\n")

question3 = ("What do cows drink?\na) Milk\nb) Water\nc) Juice","b")
answer = input(question3[0] + "\nYour answer :").strip().lower()
if answer == question3[1]:
    print("Correct!")
    score += 1
else:
    print("Incorrect! The correct answer is b) Water.")
print(f"Your current score is: {score}\n")

print(f"Thank you for playing! Your final score is: {score}/3")

input("Press Enter to exit...")
