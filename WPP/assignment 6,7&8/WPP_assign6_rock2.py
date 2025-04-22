'''Write a class called Rock_paper_scissors that implements the logic of the game Rock paper-
scissors. For this game the user plays against the computer for a certain number of rounds.

Your class should have fields for the how many rounds there will be, the current round number,
and the number of wins each player has. There should be methods for getting the computer’s
choice, finding the winner of a round, and checking to see if someone has one the (entire)
game. You may want more methods.
'''
import random

class Rock_paper_scissors():
    def __init__(self,rounds):
        self.rounds=rounds
        self.current_round=1
        self.player_wins=0
        self.computer_wins=0
        self.choices=['rock','paper','scissors']

    def get_computer_choice(self):
        return random.choice(self.choices)
    
    def find_winner(self,player_choice, computer_choice):
        if player_choice==computer_choice:
            return "draw"
        elif (player_choice == 'rock' and computer_choice == 'scissors') or \
             (player_choice == 'scissors' and computer_choice == 'paper') or \
             (player_choice == 'paper' and computer_choice == 'rock'):
            return "player"
        else:
            return "computer"
        
    def play_round(self, player_choice):
        if player_choice not in self.choices:
            return "Invalid choice"
        
        computer_choice=self.get_computer_choice()
        print(f"Computer choice: {computer_choice}")

        winner=self.find_winner(player_choice, computer_choice)

        if winner=='player':
            self.player_wins+=1
            print("You won!")
        elif winner=='computer':
            self.computer_wins+=1
            print('Computer won!')
        else:
            print("Draw")

        self.current_round+=1

    def won_game(self):
        if self.current_round>self.rounds:
            if self.player_wins>self.computer_wins:
                print(f'\nYou won: {self.player_wins}-{self.computer_wins}')
                return True
            elif self.computer_wins>self.player_wins:
                print(f"Computer won: {self.computer_wins}-{self.player_wins}")
                return True
            else:
                print(f'Draw: {self.player_wins}-{self.computer_wins}')
                return True
        return False
        
def main():
    rounds=int(input("Enter no of rounds: "))
    game=Rock_paper_scissors(rounds)

    while game.current_round<=game.rounds:
        print(f"\nRound: {game.current_round} of {game.rounds}")
        player_choice=input('Enter your choice: ')
        game.play_round(player_choice)

        if game.won_game():
            break

if __name__=="__main__":
    main()



    
        
        
        
