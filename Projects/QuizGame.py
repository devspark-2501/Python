# Project Idea: Quiz Game

print("================================")
print("       PYTHON QUIZ GAME         ")
print("================================")

name = input("What's your name? ")

score = 0

print("\nWelcome,", name, "!")
print("Answer the following questions.\n")

answer = input("1. Which language are we learning? ").lower()

if answer == "python":
    print("Correct! 🎉")
    score += 1
else:
    print("Wrong! The answer is Python.")

answer = input("\n2. What is 5 * 5? ")

if answer == "25":
    print("Correct! 🎉")
    score += 1
else:
    print("Wrong! The answer is 25.")

answer = input("\n3. Which keyword creates a function in Python? ").lower()

if answer == "def":
    print("Correct! 🎉")
    score += 1
else:
    print("Wrong! The answer is def.")

print("\n===============================")
print("           QUIZ RESULTS          ")
print("=================================")

print("Player:", name)
print("Your score:", score, "/ 3")

if score == 3:
    print("Perfect score! You're a Python legend! 🏆")
elif score >= 2:
    print("Great job! Keep learning! 🔥")
else:
    print("Keep practising. You'll get better! 💪")
