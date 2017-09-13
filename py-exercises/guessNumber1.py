import random

play_again = 'y'
while play_again == 'y':
    guess_tried = 0
    secret_number = 5# random.randint(1, 10)
    print('I am thinking of a number between 1 and 10.')
    while True:
        guess_left = 5 - guess_tried
        print('You have {} guess left.'.format(guess_left))
        if guess_tried == 5:
            print('You ran out of guesses!')
            break

        guess = int(input("What's the number? "))
        guess_tried = guess_tried + 1
        if guess == secret_number:
            print('Yes! You win!')
            break
        elif guess > secret_number:
            print('Too high. Try again.')

        elif guess < secret_number:
            print('Too low. Try again.')

    # Ensures valid input, keep asking until y or n
    while True:
        play_again = input('Do you want to play again? (y or n)')
        if play_again != 'y' and play_again != 'n':
            print('That not a valid input')
        else:
            break


print('Bye')
