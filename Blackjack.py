import random
#1. Fix Syntax problems

def create_deck():
    cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11] * 4
    random.shuffle(cards)
    return cards

def deal_card(deck):
    return deck.pop()

def calculate_score(cards):
    values = cards                              #[card[0] for card in cards]
    if sum(values) == 21 and len(cards) == 2:
        print(f"you got a Blackjack! {cards}")
        return 0
    if sum(values) > 21 and 11 in values:
        values.remove(11)
        values.append(1)
    return sum(values)

def compare(user_score, computer_score):
    if user_score == computer_score:
        return("Draw!")
    elif computer_score == 0:
        return("Lose, Dealer has Blackjack!")
    elif user_score == 0:
        return("Win, You have Blackjack!")
    elif user_score > 21:
        return("You went over. You lose!")
    elif computer_score > 21:
        return("Dealer went over. You win!")
    elif user_score > computer_score:
        return("You win!")
    else:
        return("You lose!")

def print_hand(player, cards, score):
    card_names = cards                           #[card[1] for card in cards]
    print(f"{player}'s cards: {card_names}")     #{', '.join(card_names)}")
    print(f"{player}'s score: {score}\n")

def play_blackjack():
    num_players = int(input("Enter the number of Player (1-4): "))
    if num_players <1 or num_players >4:
        print("invalid number of players")
        return
    deck = create_deck()
    player_cards = [[] for i in range (num_players)]
    computer_cards = [deal_card(deck), deal_card(deck)]

    for i in range (num_players):
        player_cards[i] = [deal_card(deck),deal_card(deck)]

    game_over = [False] * num_players

    while not all(game_over):
        for i in range(num_players):
            if not game_over[i]:
                user_score = calculate_score(player_cards[i])
                computer_score = calculate_score(computer_cards)

                print_hand(f"Player {i + 1}", player_cards[i], user_score)
                print(f"Dealer's first card: {computer_cards[0][1]}\n")

                if user_score == 0 or user_score > 21:
                    game_over[i] = True
                else:
                    user_should_deal = input(f"Player {i + 1}, type 'y' to get another card, 'n' to pass: ")
                    if user_should_deal == "y":
                        player_cards[i].append(deal_card(deck))
                        user_score = calculate_score(player_cards[i])
                        if user_score > 21:
                            game_over[i] = True
                    else:
                        game_over[i] = True

    computer_score = calculate_score(computer_cards)
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card(deck))
        computer_score = calculate_score(computer_cards)
        if computer_score > 21:
            break
    
    print(f"\n--- Final results ---\n")
    for i in range(num_players):
        user_score = calculate_score(player_cards[i])
        print_hand(f"Player {i + 1}", player_cards[i], user_score)
    
    print_hand("Dealer", computer_cards, computer_score)

    for i in range(num_players):
        user_score = calculate_score(player_cards[i])
        print(f"Player {i + 1}: {compare(user_score, computer_score)}")

play_blackjack()