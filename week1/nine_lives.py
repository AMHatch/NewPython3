import random



words = ["pizza", "fairy", "teeth", "tooth", "shirt", "otter", "batch","plane","sushi","stick","stone","style","match","hatch","emily","watch","coded","digit", "heart"]
#words = ['pizzas']
secret_word = random.choice(words)
clue = list(len(secret_word) * '?')
# clue = list('?????')
heart = u'\u2764'
guessed_word_correctly = False
list(secret_word)
unknown_letters = len(secret_word) 
lives = 9
letters_guessed =[]

while lives > 0:
    
    print(clue)
    print(lives * heart)
    
    guess = input('Guess a Letter!:')
    guess = guess.lower()
    letters_guessed.append(guess)
    print(f'Letters Guessed: {letters_guessed}')
    guess_letters = list(guess)
    
    if guess in secret_word: 
        index= 0
        while index < len(secret_word):
            if guess == secret_word[index]:
                clue[index] = guess
                unknown_letters = unknown_letters - 1
            index += 1
            
    else:
            print('That letter is incorrect, you lose a life!')
            lives -= 1
            
    if guess == secret_word or unknown_letters == 0:
        guessed_word_correctly = True
        
        print("Well! Look at you! ")
        
        print(f'The word was {secret_word}!')
        break 
    if lives == 0:
        print('You are out of lives! Please play again!')













