# -*- coding:utf-8 -*-
__author__ = 'Djj'

#一摞纸牌
import collections

Card = collections.namedtuple('Card',['rank','suit'])
suit_vaules = dict(spades=3,diamonds=2,hearts=1,clubs=0)

def spades_high(card):
    rank_value = FrenchDeck.ranks.index(card.rank)
    return rank_value * len(suit_vaules) + suit_vaules[card.suit]


class FrenchDeck:
    ranks = [str(n) for n in range(2,11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank,suit) for suit in self.suits
                                       for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]


deck = FrenchDeck()
print len(deck)

print deck[0]


from random import choice,_inst

print choice(deck)

print deck[int(_inst.random() * len(deck))]
print '_inst:' + str(_inst)
print '_inst.random():'+ str(_inst.random())
print 'len(deck):' + str(len(deck))
print int(_inst.random() * len(deck))

print deck[:3]

print deck[12::13]


for card in deck:
    print card

for card in reversed(deck):
    print card

print '********************************'

for card in sorted(deck,key=spades_high):
    print card


