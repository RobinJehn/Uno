import random

class AI():
    
    def __init__(self):
        print('created')
    
    def play(self, player, game):
        current_str = game.discard_pile[-1].str
        # Handle last player played +2
        if current_str == '+2' and game.draw_amount > 0:
            # Try playing +2
            playable_cards = player.getPlusTwos()
            if len(playable_cards) > 0:
                card_to_play = random.choice(playable_cards)
                player.playCard(card_to_play, game)
            else: # Otherwise draw
                player.drawCards(game, game.draw_amount)
                game.resetDrawAmount()
                
        # Handle last player played +4        
        elif current_str == '+4' and game.draw_amount > 0:
            # Try playing +4
            playable_cards = player.getPlusFours()
            if len(playable_cards) > 0:
                card_to_play = random.choice(playable_cards)
                player.playCard(card_to_play, game)
            else: # Otherwise draw
                player.drawCards(game, game.draw_amount)
                game.resetDrawAmount()
        else:
            # Play a random of the playable cards
            playable_cards = player.playableCards(game)
            if len(playable_cards) > 0:
                card_to_play = random.choice(playable_cards)
                player.playCard(card_to_play, game)
            else: # Otherwise draw
                player.drawCards(game, 1)
        return player.hasWon()