import random

def hangman():
    word_list = ['python', 'hangman', 'programming', 'developer', 'computer', 'science']
    
    # Randomly choose a word from the list
    word_to_guess = random.choice(word_list)
    
    # Create a list of underscores to represent the hidden word
    guessed_word = ['_'] * len(word_to_guess)
    
    attempts = 6
    guessed_letters = []
    
    print("Welcome to Hangman!")
    print("Try to guess the word!")
    
    while attempts > 0:
        print("\nCurrent word: " + ' '.join(guessed_word))
        print(f"Guessed letters: {', '.join(guessed_letters)}")
        print(f"Attempts remaining: {attempts}")
        
        # Ask the user to guess a letter
        guess = input("Enter a letter: ").lower()
        
        # Check if the guess is valid
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter only one letter.")
            continue
        
        # Check if the letter was already guessed
        if guess in guessed_letters:
            print("You've already guessed that letter. Try again.")
            continue
        
        # Add the guess to the list of guessed letters
        guessed_letters.append(guess)
        
        # Check if the guessed letter is in the word
        if guess in word_to_guess:
            print(f"Good guess! The letter '{guess}' is in the word.")
            
            # Reveal the guessed letter in the word
            for i in range(len(word_to_guess)):
                if word_to_guess[i] == guess:
                    guessed_word[i] = guess
        else:
            print(f"Oops! The letter '{guess}' is not in the word.")
            attempts -= 1
        
        # Check if the word is fully guessed
        if '_' not in guessed_word:
            print(f"\nCongratulations! You've guessed the word: {''.join(guessed_word)}")
            break
    
    if attempts == 0:
        print(f"\nGame Over! The word was: {word_to_guess}")

# Run the game
hangman()
