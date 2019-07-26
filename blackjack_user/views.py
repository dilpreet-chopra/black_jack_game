# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
import class_based_view
from django.http import HttpResponse,HttpResponseRedirect
import json

bj=class_based_view.Blackjack()
def home(request):
	return render(request,'black-jack.html')

def randomization(request):
	list_cards=bj.find_random_cards()
	print ('list of random cards',list_cards)
	response = HttpResponse(json.dumps(list_cards))	
	return response	
def card_of_deck(request):
	print "############", request
	card_from_deck=bj.card_from_deck()
	print ('deck_card',card_from_deck)
	response = HttpResponse(json.dumps(card_from_deck))	
	return response	
