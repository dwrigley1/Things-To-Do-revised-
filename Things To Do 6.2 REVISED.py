# This program compares the values contained in two variables and uses a 'while True' loop to continuously
# iterate through the loop until the values are equal then ends
# number 6.2 in 'Things To Do'

guess_me = 7
number = 1

while True:
    if number == guess_me:
        print("found it!")
        break
    elif number < guess_me:
        print("too low")
        number +=1
    else:
        # this condition would only be met if the value of number was greater than guess_me
        print("oops!")
        break
