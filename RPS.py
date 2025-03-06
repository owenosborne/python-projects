import random
user_wins = 0
computer_wins = 0
options = ['rock', 'paper', 'scissors']



while True:
    user_input = input("Rock, Paper, Scissors or Q to quit: ").lower()
    if user_input == 'q':
        break

    if user_input not in ['rock', 'paper', 'scissors']:
        continue

    random_number = random.randint(0, 2)
    # 0 is rock, 1 is paper, 2 is scissors
    computer_chose = options[random_number]
    print('computer picked', computer_chose + '.')

    if user_input == 'rock' and computer_chose == 'scissors':
        print('You Win!')
        user_wins += 1
    if user_input == 'scissors' and computer_chose == 'paper':
        print('You Win!')
        user_wins += 1
    if user_input == 'paper' and computer_chose == 'rock':
        print('You Win!')
        user_wins += 1

    if user_input == 'rock' and computer_chose == 'paper':
        print('You loose! Try again: ')
        computer_wins += 1
    if user_input == 'scissors' and computer_chose == 'rock':
        print('You loose! Try again:')
        computer_wins += 1
    if user_input == 'paper' and computer_chose == 'scissors':
        print('You loose! Try again: ')
        computer_wins += 1

    if user_input == 'rock' and computer_chose == 'rock':
        print('A draw! Try again: ')
        user_wins += 1
    if user_input == 'scissors' and computer_chose == 'scissors':
        print('A draw! Try again:')
        user_wins += 1
    if user_input == 'paper' and computer_chose == 'paper':
        print('A draw! Try again: ')
        user_wins += 1


print('You won', user_wins, 'times.')
print('The computer won', computer_wins, 'times.')

print('Bye!')