class Card():

    def __init__(self, colour, str):
        self.colour = colour
        self.str    = str

    def isPlayable(self, game):
        top_card = game.discard_pile[-1]
        return self.colour == 'black' or game.current_colour == self.colour or top_card.str == self.str
    
    def display(self):
        print(f"{self.colour} {self.str}")