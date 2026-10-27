# Day 01

questions = ('What is the capital of France',
             'What is the capital of India',
             'What is the capital of USA',
             'What is the capital of Germany',
            #  'What is the capital of Italy'
            )

options = (
    ('A. Paris', 'B. London', 'C. Berlin', 'D. Madrid'),
    ('A. New Delhi', 'B. Mumbai', 'C. Kolkata', 'D. Chennai'),
    ('A. Washington D.C.', 'B. New York', 'C. Los Angeles', 'D. Chicago'),
    ('A. Berlin', 'B. Munich', 'C. Frankfurt', 'D.Hamburg')
)

answer = ('A', 'A', 'A', 'A')
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