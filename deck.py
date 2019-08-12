import copy
import random

class Deck:

    def __init__(self):
        self.suits = ["\u2660", "\u2661", "\u2662", "\u2663", ]  # spades, hearts, diamonds, clubs
        self.cards = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
        self.deck_suits = [x + str(y) for x in self.suits for y in self.cards]
        self.deck_books = [y + str(x) for x in self.cards for y in self.suits]
        self.play_deck = copy.copy(self.deck_suits)
        self.players_dict = dict()
        self.num_players = 0
        
    def make_hands(self, players=4):
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
        if sort_by == 'cards':
            self.tuples_deck = [(x, y) for x, y in zip(range(52), self.deck_books)]
        else:
            self.tuples_deck = [(x, y) for x, y in zip(range(52), self.deck_suits)]
        for player in self.players_dict.keys():
            self.placeholder = []
            for card in self.players_dict[player]:
                for tuple in self.tuples_deck:
                    if card in tuple:
                        self.placeholder.append(tuple)
            self.players_dict[player] = sorted(self.placeholder)
            self.players_dict[player] = [y for x, y in self.players_dict[player]]