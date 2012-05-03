#Prompt:
# We all know the classic "guessing game" with higher or lower prompts. lets 
# do a role reversal; you create a program that will guess numbers between 
# 1-100, and respond appropriately based on whether users say that the number 
# is too high or too low. Try to make a program that can guess your number 
# based on user input and great code!

def guess(low, high):
    current_guess = (high + low) / 2
    print("I think your number is %d." % current_guess)
    print("Correct [c], Too High [h], Too Low [l]")
    answer = raw_input().lower()

    if answer == 'c':
        print("I knew your number was %d." % current_guess)
    elif answer == 'h':
        guess(low, current_guess)
    elif answer == 'l':
        guess(current_guess, high)
    else:
        print("I stumped...")


print("Pick a number between 1 - 100")
guess(1,100)
