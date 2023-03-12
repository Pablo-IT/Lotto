import random

#probability of draving all six numbers
numbers_count = [49, 48, 47, 46, 45, 44]
numbers_count_to_draw = [6, 5, 4, 3, 2, 1]

probability_count = 1
probability_to_draw = 1

for number in numbers_count:
    nr = number * 1
    probability_count *= nr

for number in numbers_count_to_draw:
    nr = number * 1
    probability_to_draw *= nr

probability = int(probability_count / probability_to_draw)

#generating 49 numbers
numbers_range = range(50)
numbers = list(numbers_range)
numbers.pop(0)

#Drawing random six numbers
drawn_numbers = []
nr = 0
while (nr < 6):
    drawn = (random.randint(1,49))
    if drawn not in drawn_numbers:
        drawn_numbers.append(drawn)
        nr += 1
    else:
        continue

#Draving six numbers choosen by user
user_numbers = []
nr = 0

while nr < 6:
    user_drawn = input('Please type a number from 1 to 49:')
    if user_drawn.isnumeric():
        user_drawn = int(user_drawn)
        if (user_drawn < 1 or user_drawn > 49):
            print('Number needs to be in range from 1 to 49.')
        elif user_drawn not in user_numbers:
            user_numbers.append(user_drawn)
            nr += 1
        else:
            print('This value has been already chosen.')
    else:
        print('Value has to be a number in range from 1 to 49.')

#User results
drawn_numbers.sort()
user_numbers.sort()

result = []

for number in drawn_numbers:
    if number in user_numbers:
        result.append(number)

result.sort()
result_count = len(result)

#Probability of user results
probability_count_r = 1
probability_draw_r = 1

user_probability_range = numbers_count[0:result_count]
user_numbers_range = range(result_count + 1)
user_drawn_numbers = list(user_numbers_range)
user_drawn_numbers.pop(0)

for number in user_probability_range:
    nr = number * 1
    probability_count_r *= nr

for number in user_drawn_numbers:
    nr = number * 1
    probability_draw_r *= nr

userp = 1/(probability_count_r / probability_draw_r)
userp = '{:.2%}'.format(userp)

#Print results
print('Probability of drawing a six is 1:', probability)

if result_count > 0:
    print('Probability of drawing a: ', result_count, ' is: ', userp)
    print('Drawn numbers: ', drawn_numbers)
    print('Your numbers: ', user_numbers)
    print('You drew: ', result_count, 'on 6 numbers. Lucky numbers: ', result)
else:
    print('Bad luck! Try again!')