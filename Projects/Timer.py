# Project Idea: Timer

# import time

# time.sleep(1)
# for x in range(0, 60):
#     Check = (input('To Check Time (T): '))
#     if (Check == 'T') or (Check == 't'):
#         print(x)
# import time

# for x in range(1, 61):
#     time.sleep(1)
#     check = input("Press T to check time: ")

#     if check.lower() == 't':
#         print("Current Time:", x)

import time

myTime = int(input('Enter Time in Seconds: '))
for x in range(myTime, 0, -1):
    print(x)
    time.sleep(1)
print('TIME UP!!')