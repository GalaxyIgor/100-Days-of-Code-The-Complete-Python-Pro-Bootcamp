def get_card_data():
    cards = {
        "ace": 0,
        "2": 2,
        "3": 3,
        "4": 4,
        "5": 5,
        "6": 6,
        "7": 7,
        "8": 8,
        "9": 9,
        "10": 10,
        "jack": 10,
        "queen": 10,
        "king": 10,
    }
    return cards

def get_random_cards():
    import random
    cards = list(get_card_data().keys())
    random_cards = random.sample(cards, 2)
    return random_cards

def calculate_hand_value(cards):
    card_data = get_card_data()
    total = 0

    total += sum(card_data[card] for card in cards)
    
    for card in cards:
        if card == "ace":
            if total + 11 <=21:
                total += 11 
            else:
                total += 1
    return total

def deal_card():
    import random
    cards = list(get_card_data().keys())
    return random.choice(cards)
    
def main():
    user_cards = get_random_cards()
    computer_cards = get_random_cards()
    user_score = 0
    computer_score = 0

    game_over = False
    while not game_over:
        print(f"Your cards: {user_cards}, current score: {calculate_hand_value(user_cards)}")

        if calculate_hand_value(user_cards) > 21:
            game_over = True
            continue

        should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
        if should_deal == "y":
            user_cards.append(deal_card())
        else:
            game_over = True

    if calculate_hand_value(user_cards) <= 21:
        while calculate_hand_value(computer_cards) < 17:
            computer_cards.append(deal_card())

    print(f"Your final hand: {user_cards}, final score: {calculate_hand_value(user_cards)}")
    print(f"Computer's final hand: {computer_cards}, final score: {calculate_hand_value(computer_cards)}")

    if calculate_hand_value(user_cards) > 21:
        computer_score += 1
    elif calculate_hand_value(computer_cards) > 21:
        user_score += 1
    elif calculate_hand_value(user_cards) > calculate_hand_value(computer_cards):
        user_score += 1
    elif calculate_hand_value(computer_cards) > calculate_hand_value(user_cards):
        computer_score += 1

    print(f"User score: {user_score}, Computer score: {computer_score}")


play_again = "y"
while play_again == "y":
    main()
    play_again = input("Type 'y' to play again, type 'n' to quit: ")

