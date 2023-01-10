import random 


chosen_number = random.randint(0,100)

live = 5
is_game_over = False
while not is_game_over:
    if live < 1:
        print('-----------')
        print('you lose.')
        print('-----------')
        is_game_over = True
    else:
        user_guess = int(input(f'enter number(you have {live}): '))
        if user_guess == chosen_number:
            print('well done your right!')
            is_game_over = True
        
        if user_guess < chosen_number:
            print("it's Larger")
            live -= 1
        elif user_guess > chosen_number:
            live -= 1
            print("it's smaller")