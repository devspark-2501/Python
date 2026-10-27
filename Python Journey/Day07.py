# Basic Pyhton Quiz App

questions = ('How many elements are there in perodic table',
             'Which animal lays the largest egg',
             'What is the most abudant gas in earth atmosphere',
             'How many bones are there in human body',
             'Which planet in solar system is the hottest'
            )
options = (
    ('A. 166','B. 117','C. 118','D. 119'),
    ('A. Whale','B. Ostrich','C. Eagle','D. Lion'),
    ('A. Nitrogen','B. Oxygen','C. Carbon dioxide','D. Sulfur'),
    ('A. Mars','B. Venus','C. Sun','D. Earth')
)

answer = ('C','B','A','A','B')
guesses = []
score = 0
question_num = 0

for question in questions:
    print('----------------------')
    print(question)
    for option in options:
        print(option)

guess = input('Enter (A, B, C, D): ')
guesses.append(guess)
if guess == answer[question_num]:
    score += 10
    print('CORRECT !!')
else:
    print('INCORRECT !!')
    print(f'{answer[question_num]} is the correct answer')

question_num += 1