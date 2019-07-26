from django.conf.urls import url
from blackjack_user import views

urlpatterns = [
url(r'^$',views.home),
url(r'^blackjack/',views.home),
url(r'^randomization/',views.randomization,name='randomization'),
url(r'^deck_card/',views.card_of_deck,name='deck_card'),
]