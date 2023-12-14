# card_deck = {24, 9, 8, 4, 6, 3, 44, 3}
# hand = []
#
# while sum(hand) <= 34:
#     hand.append(card_deck.pop())
# hello = sum(hand)
# print(hand, hello)

headlines = ["Local Bear Eaten by Man",
             "Legislature Announces New Laws",
             "Peasant Discovers Violence Inherent in System",
             "Cat Rescues Fireman Stuck in Tree",
             "Brave Knight Runs Away",
             "Papperbok Review: Totally Triffic"]

news_ticker = ""
for headline in headlines:
    news_ticker += headline + " "
    if len(news_ticker) >= 140:
        news_ticker = news_ticker[:150] + "..."
        break


print(news_ticker)