'''
Samuel Narvaez
BYUI CSE210 W2 Prove
Tic-Tac-Toe
'''

import random  

def main():
    print("Tic-Tac-Toe")
    law = ""
    randomer = ("x", "o")
    randomer = (random.choice(randomer))
    law = randomer
    table_data = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    table(table_data)
    players_start(law,table_data)
    players_start(next_player_turn(law), table_data)
    players_start(law, table_data)
    players_start(next_player_turn(law), table_data)
    players_start(law, table_data)
    winner(law, table_data, game_over())
    players_start(next_player_turn(law), table_data)
    winner(next_player_turn(law), table_data, game_over())
    players_start(law, table_data)
    winner(law, table_data, game_over())
    players_start(next_player_turn(law), table_data)
    winner(next_player_turn(law), table_data, game_over())
    players_start(law, table_data)
    winner(law, table_data, game_over())
    
    print("Its a draw ,Both Players Win.")
    play_again()

def winner(player,table_data,game_over):
    if table_data[0] == table_data[1] == table_data[2]:
        print(f"{player.capitalize()} won, {game_over} ")
        play_again()       
        
    elif table_data[3] == table_data[4] == table_data[5]:
        print(f"{player.capitalize()} won, {game_over} ")
        play_again()
        
    elif table_data[6] == table_data[7] == table_data[8]:
        print(f"{player.capitalize()} won, {game_over} ")
        play_again()
        
    elif table_data[0] == table_data[3] == table_data[6]:
        print(f"{player.capitalize()} won, {game_over} ")
        play_again()
         
    elif table_data[1] == table_data[4] == table_data[7]:
        print(f"{player.capitalize()} won, {game_over} ")
        play_again()
        
    elif table_data[2] == table_data[5] == table_data[8]:
        print(f"{player.capitalize()} won, {game_over} ")
        play_again()
        
    elif table_data[0] == table_data[4] == table_data[8]:
        print(f"{player.capitalize()} won, {game_over} ")
        play_again()
        
    elif table_data[2] == table_data[4] == table_data[6]:
        print(f"{player.capitalize()} won, {game_over} ")
        play_again()
        
def table(table_data):
    print("-------------")
    print("|", table_data[0], "|", table_data[1], "|", table_data[2], "|",)
    print(" ---+---+---")
    print("|", table_data[3], "|", table_data[4], "|", table_data[5], "|",)
    print(" ---+---+---")
    print("|", table_data[6], "|", table_data[7], "|", table_data[8], "|",)
    print("-------------")

def players_start(player, table_data):
    if player == "x" or player == "o":
        loop = ''
        while loop != False:
            choice = get_inp(player, table_data)
            if choice not in table_data:
                print("try another block")
                loop = True
            else:
                table_data[choice - 1] = player
                return (table(table_data))
                #loop = False

def get_inp(player, table_data):
    loop_num = ""
    while loop_num != True:
        get_input = input(f"{player}'s turn to choose a square (1-9): ")
        if get_input.isdigit():
            if int(get_input) > 0 and int(get_input) < 10:
                if int(get_input) in table_data:
                    get_input = int(get_input)
                    loop_num = True
                    return get_input
            else:
                print("Try Again.Seems like you have entered Invalid key.")
                loop_num = False
        else:
            print("Try Again.")
            loop_num = False

def next_player_turn(randomiser):
    if randomiser == "" or randomiser == "o":
        return "x"
    elif randomiser == "x":
        return "o"

def game_over():
    greet = ["Fatality.",
             "Every winner has their day.",
             "It's my game."
             "Good game. Thanks for playing!",
             "Well the end of ages of war.",
             "Look I'm the King here.",
             "Well,That was so easy"]
    won = random.choice(greet)
    return won

def play_again():
    play_again = input("Want to play again ? Reply Y for yes / N or Enter Key for No : ")
    if play_again.lower() == "y":
        print("New Game Start")
        main()
    else:
        print("Thanks for playing :) ")
        exit()

if __name__ == "__main__":
    main()