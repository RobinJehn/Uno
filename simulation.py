import Game
import AI

n_simulations = 100000
ai = AI.AI() # Initialize random AI
players = { 'Milla': 0, 'Robin': 0, 'Anke': 0, 'Frida': 0 }
for i in range(n_simulations):
    game = Game.Game(players.keys())

    while True:
        if ai.play(game.current_player, game): # returns true if player has won
            players[game.current_player.name] += 1
            break
        game.nextPlayer()
    
# Calculate and display win percentages
win_percentage = {key: round((value/n_simulations)*100, 2) for key, value in players.items()}
print(win_percentage)

