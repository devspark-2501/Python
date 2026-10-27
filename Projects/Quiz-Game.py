# Project Idea: Quiz Game

questions = ('How many elements are their in perodic table',
    'Which animal lays the largest egg',
    'What is the most abundant gas in earth atmosphere',
    'How many bones are their in human body',
    'Which planet in solar system is the hottest')

options = (
    ('A. 116','B. 117','C. 118','D. 119'),
    ('A. Whale','B. Ostrich','C. Eagle','D. Lion'),
    ('A. Nitrogen','B. Oxygen','C. Carbon dioxide','D. Sulfur'),
    ('A. 206','B. 207','C. 208','D. 209'),
    ('A. Mars','B. Venus','C. Sun','D. Earth')
)

answer = ('C', 'B', 'A', 'A', 'B')
guesses = []
score = 0
question_num = 0

for question in questions:
    print('----------------------')
    print(question)
    for option in options[question_num]:
        print(option)
    
    guess = input('Enter (A, B, C, D): ').upper()
    guesses.append(guess)
    if guess == answer[question_num]:
        score += 5
        print('CORRECT !!')
    else:
        print('INCORRECT !!')
        print(f'{answer[question_num]} is the correct answer')


    question_num += 1