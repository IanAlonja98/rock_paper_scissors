import random

def play():
    user = input("What's your choice? 'r' for rock, 'p' for paper, and 's' for scissors\n")
    computer = random.choice(['r', 'p', 's'])

    if user == computer:
        return 'It\'s a draw!!!'

    if hav_won(user,computer):
        return 'You have won!!!!'

    return 'You have lost!!!!'

    #we know that rocks > scissors, scissors > paper, paper > rock

def hav_won(player, opponent):

    #should return true if the player wins
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p')  or (player == 'p' and opponent == 'r'):
        return True


#we need to call the function to run the program
print(play())