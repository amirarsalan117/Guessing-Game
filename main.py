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
        