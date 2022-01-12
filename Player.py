import random

class Player():

    def __init__(self, name):
        self.hand = []
        self.name = name
        
    def hasWon(self):
        return len(self.hand) == 0
    
    def drawCards(self, game, amount):
        cards = game.draw(amount)
        self.hand += cards
        #print(f"{self.name} draws {amount} cards and now has {len(self.hand)} cards")
        
    def displayHand(self):
        print(f"Player {self.name}'s hand:")
        print('-' * 40)
        for card in self.hand:
            card.display()
        print('-' * 40)
        
    def playableCards(self, game):
        cards = []
        for card in self.hand:
            if card.isPlayable(game):
                cards.append(card)
        return cards
        
    def getPlusTwos(self):
        cards = []
        for card in self.hand:
            if card.str == '+2':
                cards.append(card)
        return cards
    
    def getPlusFours(self):
        cards = []
        for card in self.hand:
            if card.str == '+4':
                cards.append(card)
        return cards
    
    def playCard(self, card, game):
        #print(f"{self.name}({len(self.hand)} -> {len(self.hand) - 1}) plays ", end="")
        self.hand.remove(card)
        game.discard_pile.append(card)
        #card.display()
        
        # Handle colour
        if card.colour == 'black':
            game.randomColour()
        else:
            game.current_colour = card.colour
          
        # Handly Type
        if card.str == 'reverse':
            game.reverse()
        elif card.str == 'skip':
            game.skip()
        elif card.str == '+2':
            game.draw_amount += 2
        elif card.str == '+4':
            game.draw_amount += 4
        
        
        
        