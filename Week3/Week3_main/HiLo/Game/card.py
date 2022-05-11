import random

class Card:
    """A small card with a value between 1 and 13.
    
    The responsibility of the Card is to keep track of the value of the current and the next card.
    
    Attributes:
        value (int): The number value on the card.
        suit (string): The suit on the card.
    """
    def __init__(self):
        """Constructs a new instance of Card.
        
        Args:
            self (Card): An instance of Card.
        """
        self.value = 0
        self.suit = ""

    def draw(self):
        self.value = random.randint(1,13)


    def suits(self):
        suits = ["Hearts", "Clubs", "Spades", "Diamonds"]
        self.suit = random.choice(suits)
        return self.suit
        
            



