# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import random

class Blackjack():
	cards=[2,3,4,5,6,7,8,9,10,'ace','king','queen','jack']
	shapes=['hearts','diamonds','spades','clubs']
	def find_random_cards(self):
		list_cards=[]
		for i in range(0,3):
			card=random.choice(self.cards)
			shape=random.choice(self.shapes)
			temp=str(card)+' of '+shape
			list_cards.append(temp)
		return list_cards	
			
	def card_from_deck(self):
		card=random.choice(self.cards)
		shape=random.choice(self.shapes)
		card_from_deck=str(card)+' of '+shape
		return card_from_deck

	# def logic_blackjack(self):
		 	

			