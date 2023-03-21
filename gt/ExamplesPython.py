
#!Draw Program
# import random

# names = input("Enter usernames with spaces: ")
# names = names.split(" ")
# winners_numbers = int(input("How many winners will there be: "))
# spares_numbers = int(input("How many spares will there be: "))

# Winners = random.sample(names, winners_numbers)
# Spares = []
# for name in names:
#     if name not in Winners:
#         Spares.append(name)
#     if len(Spares) == spares_numbers:
#         break

# print("Winners: ", Winners)
# print("Spares: ", Spares)

#* Let the user be asked to choose cinema or theater.
#*$50 to watch movies,
#*$100 is required for the theater.
#*Considering that students are given a 50% discount
#*student discount
#*amount without discount if not a student
#*Write the code that calculates and prints it to the screen.

# while True:
#     print("Which would you like to watch?")
#     print("Cinema (c) Theatre (t)")
    
#     choice = input("Make your selection: ")
#     discount = input("Are you a student? (y/n): ")
#     print("Cinema: $50, Theatre: $100")
            
#     if choice == "c":
#         if discount == "y":
#             print("Your discounted price is: $25. Enjoy the show!")
#         else:
#             print("Your price is: $50. Enjoy the show!")
#     elif choice == "t":
#         if discount == "y":
#             print("Your discounted price is: $50. Enjoy the show!")
#         else:
#             print("Your price is: $100. Enjoy the show!")
#     else:
#         print("We didn't understand your request, please try again.")
        
#     answer = input("Would you like to perform another operation? (y/n): ")
#     if answer == "n":
#         break

#!Weather State
# import datetime

# Weather = ["Sun","Rain","Snow"]
# rndWe = random.choice(Weather)
# if rndWe == "Sun":
#     print("Today is Sunny be relax :)")
# elif rndWe == "Rain":
#     print("Today is Rainy take umbrella")
# elif rndWe == "Snow":
#     print("Today is Snow be careful")
# else:
#     print("Error Check Code")

#!BlackJack Game
# import random

# # Game cards
# cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 11]

# def distribute_card():
#     return random.choice(cards)

# def calculate_hand_total(hand):
#     if 11 in hand and sum(hand) > 21:
#         hand.remove(11)
#         hand.append(1)
#     return sum(hand)

# def blackjack():
#     print("Welcome to Blackjack!")
    
#     player_cards = [distribute_card(), distribute_card()]
#     print("Player's cards: ", player_cards)
    
#     dealer_cards = [distribute_card()]
#     print("Dealer's cards: ", dealer_cards)
    
#     while True:
#         request = input("Do you want a card? (Y/N) ")
#         if request.lower() == 'y':
#             player_cards.append(distribute_card())
#             print("Player's cards: ", player_cards)
#             if calculate_hand_total(player_cards) > 21:
#                 print("Hand total: ", calculate_hand_total(player_cards))
#                 print("Bust!")
#                 return
#         else:
#             break
    
#     while calculate_hand_total(dealer_cards) < 17:
#         dealer_cards.append(distribute_card())
    
#     player_total = calculate_hand_total(player_cards)
#     dealer_total = calculate_hand_total(dealer_cards)
#     print("Player's hand total: ", player_total)
#     print("Dealer's hand total: ", dealer_total)
    
#     if player_total > 21:
#         print("Bust!")
#     elif player_total == dealer_total:
#         print("Push! It's a tie.")
#     elif player_total > dealer_total or dealer_total > 21:
#         print("Player wins!")
#     else:
#         print("Dealer wins!")
    
# blackjack()

