import collections

Card = collections.namedtuple('Card', ['rank', 'suit'])

class FrenchDeck:
	ranks = [str(i) for i in range(2, 11)] + list('JQKA')
	suits = 'spades diamonds clubs hearts'.split()

	def __init__(self):
		self._cards = [Card(rank, suit) for rank in self.ranks
		                                for suit in self.suits]
	def __len__(self):
		return len(self._cards)

	def __getitem__(self, item):
		return self._cards[item]


def spades_high(card):
	suit_value = dict(spades=3, hearts=2, diamonds=1, clubs=0)
	print(suit_value)
	rank_value = FrenchDeck.ranks.index(card.rank) ##获取牌面值0-12
	return rank_value*len(suit_value) + suit_value[card.suit]

if __name__ == '__main__':
	deck = FrenchDeck()
	#spades_high(Card('7', 'spades'))
	for card in sorted(deck, key=spades_high):
		print(card)

