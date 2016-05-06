print 'Please think of a number between 0 and 100!'
number = 0
higher = 100
lower = 0
answer = 'l'
while answer != 'c':
    if answer == 'l':
        lower = number
    elif answer == 'h':
        higher = number
    else:
        print 'Sorry, I did not understand your input.'
    number = (higher + lower)/2
    print ('Is your secret number ' + str(number) + '? ')
    answer = raw_input ('Enter \'h\' to indicate the guess is too high. Enter \'l\'to indicate the guess is too low. Enter \'c\' to indicate I guessed correctly. ')
print 'Game over. Your secret number was: ' +str(number)