# This program looks for either True or False values to be added to the variables 'green' and 'small' 
# depending on which value equals True and which equals False will alter the output 
# number 4.2 in 'Things To Do'

small = False
green = True

if small and green:
    print("pea is a match")
elif not small and green:
    print("watermelon is a match")
elif small and not green:
        print("cherry is a match")
else:
     print("pumpkin is a match")