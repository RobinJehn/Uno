import Card
import Player
from numpy import *
import random

class Game():

    def __init__(self, players, starting_cards = 7):
        self.deck = []
        self.discard_pile = []
        self.players = []
        self.n_players = len(players)
        self.direction = 1 # 1 clockwise/0 counterclockwise
        self.draw_amount = 0

        self.initializeDeck()
        self.initializePlayers(players, starting_cards)
        self.startGame()
        
        
        
    def startGame(self):
        # Reveal first card
        first_card = self.deck.pop()
        self.discard_pile.append(first_card)
        self.handleFirstCard(first_card)  
            
    def handleFirstCard(self, first_card):
        # Handle the type
        if first_card.str == '+2':
            self.current_player.drawCards(self, 2)
            self.skip()
        elif first_card.str == '+4':
            self.current_player.drawCards(self, 4)
            self.skip()
        elif first_card.str == 'skip':
            self.skip()
        elif first_card.str == 'reverse':
            self.reverse
           
        # Handle the colour
        if first_card.colour == 'black':
            self.randomColour()
        else:    
            self.current_colour = first_card.colour
                      
    def randomColour(self):
        self.current_colour = random.choice(['red', 'green', 'blue', 'yellow'])
            
    def resetDrawAmount(self):
        self.draw_amount = 0
        
    def reverse(self):
        self.direction *= -1
        
    def skip(self):
        self.nextPlayer()
      
    def initializeDeck(self):
        self.addColouredCards()
        self.addBlackCards()
        random.shuffle(self.deck)
        
    def initializePlayers(self, players, starting_cards):
        for name in players:
            player = Player.Player(name)
            self.players.append(player)
            player.drawCards(self, starting_cards)
        self.current_player = self.players[0]
        
    def nextPlayer(self):
        # Use the direction of the game to find the next player
        current_index = self.players.index(self.current_player)
        new_index = (current_index + self.direction) % self.n_players # 4 wraps around to 1 through modulo
        self.current_player = self.players[new_index]

    def addColouredCards(self):
        colours = ['red', 'green', 'blue', 'yellow']
        strs = list(range(10)) + list(range(1,10)) + ['skip', 'reverse', '+2'] * 2
        for colour in colours:
            for str in strs:
                card = Card.Card(colour, str)
                self.deck.append(card)
    
    def addBlackCards(self):
        strs = ['+4', 'colour']
        for str in strs:
            for i in range(4):
                card = Card.Card('black', str)
                self.deck.append(card)
    
    def displayDeck(self):
        print('Deck: ')
        print('-' * 40)
        for card in self.deck:
            card.display()
        print('-' * 40)
            
    def reshuffle(self):
        # Leave the top card on the discard pile
        remaining_card = self.discard_pile.pop()
        other_cards = self.discard_pile.copy()
        self.discard_pile = [remaining_card]
        
        # Shuffle the other cards and put them into the deck
        random.shuffle(other_cards)
        self.deck = other_cards
    
    def draw(self, amount):
        cards = []
        for i in range(amount):
            if len(self.deck) == 0: # No cards left to draw
                self.reshuffle()
            card = self.deck.pop()
            cards.append(card)
        return cards
        
    def showTopCard(self):
        self.discard_pile[-1].display()