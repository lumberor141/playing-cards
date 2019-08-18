import random

class Deck:
    '''A class for making a standard 52 card deck and manipulating it.
        Contains a class for dealing cards and a class for sorting the hands.
    '''
    
    def __init__(self):
        self.suits = ["\u2660", "\u2661", "\u2662", "\u2663", ]  # spades, hearts, diamonds, clubs
        self.cards = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
        self.deck_suits = [x + str(y) for x in self.suits for y in self.cards]
        self.deck_books = [y + str(x) for x in self.cards for y in self.suits]
        self.play_deck = self.deck_suits[:]
        self.players_dict = dict()
        self.num_players = 0
        
    def make_hands(self, players=4): #add key that will control how many cards are dealt to each player
        '''The "players" key determines how many players are being dealt to.'''
        self.num_players = players
        random.shuffle(self.play_deck)        
        self.players_dict = {'player'+str(num): [] for num in range(1,self.num_players+1)}
        index = 1
        # add a card count so that each player has same amount if players doesn't / into 52
        for card in self.play_deck:
            if index == self.num_players+1:
                index = 1
            self.players_dict['player' + str(index)].append(card)
            index += 1

    def sort(self, sort_by='suits'):
        '''A method that sorts the cards in each player's hand.
            "sort_by" key determines if the hands are sorted by suit or number.
        '''
        #create a tuple deck, giving each card a number 0-51 for example (0, ♠2)
        if sort_by == 'cards':
            self.tuples_deck = [(x, y) for x, y in zip(range(52), self.deck_books)]
        else:
            self.tuples_deck = [(x, y) for x, y in zip(range(52), self.deck_suits)]
        for player in self.players_dict.keys():
            #create a placeholder list which appends the corresponding tuple for each card in player's hand
            self.placeholder = [card_tuple for card in self.players_dict[player]
                                for card_tuple in self.tuples_deck if card in card_tuple]
            #replace hand with sorted placeholder list
            self.players_dict[player] = [y for x, y in sorted(self.placeholder)]
