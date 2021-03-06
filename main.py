import random
from words import words_list


def guesstheword():
    selected_word = random.choice(words_list)
    lives = 3
    print("****Guess the Word game****\n\nTry to guess the given word. First letter is solved for you.\nGuess wisely, you can't do mistake more than 3 times. Good luck!\n\n"
        + "your life: " + str(lives) + "\n")

    display = [selected_word[0]]

    #create display list with "_"
    for i in range(len(selected_word)-1):
        display.append("_")
    print(display)

    gameover = False

    #loop until gameover=True
    while not gameover:
        guess = input("\nguess a letter: ").lower() #taking input in lowercase

        #checking if guessed letter is correct or not
		#if correct put letter in it's position of the word.
        for position in range(len(selected_word)):
            letter = selected_word[position]
            if letter == guess:
                display[position] = letter

        #if guessed letter is wrong deduct a life
        if guess not in selected_word:
            lives -= 1
            print("\nTry again\n  Remaining life: " + str(lives))
            if lives <= 0:
                gameover = True
                print(f"\nGame Over!\nThe word was '{selected_word}'.\n")

        print(display)

        #checking if all "_" filled wiht letters
        if "_" not in display:
            gameover = True
            if lives >= 3:
                print("\n***Looks like someone's on Fire!***\nGreat WIN.")
            else:
                print("\n----You've WON!----")


while True:
    guesstheword()
    while True:
        answer = str(input('\nWant to play again? (y/n): '))
        if answer in ('y', 'n'):
            break
        print("invalid input.")
    if answer == 'y':
        guesstheword()
    else:
        print("Bye. Have a good day.")
        break