# This program uses a 'for' loop to iterate oiver range(10) until the variables 
# guess_me and number are equal to each other
# number 6.3 in 'Things To Do'

guess_me = 5

for number in range(10):
    if number < guess_me:
        print("too low")
    elif number == guess_me:
        print("found it!")
        break
    else:
        print("oops!")