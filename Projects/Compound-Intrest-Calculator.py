# Project Idea: Compound Intrest Calulator

Principle = 0
Rate = 0
Time = 0

while Principle <= 0:
    Principle = float(input('Enter The Principle Amount: '))
    if Principle <= 0:
        print('Principle cant be zero or less than zero')

while Rate <= 0:
    Rate = float(input('Enter The Intrest Rate: '))
    if Rate <= 0:
        print('Rate cant be zero or less than zero')

while Time <= 0:
    Time = float(input('Enter Time in Years: '))
    if Time <= 0:
        print('Time can be zero or less than zero')

Total = Principle * pow((1 + Rate / 100), Time)
print(f'(Total Amount: ${round(Total, 2)})')