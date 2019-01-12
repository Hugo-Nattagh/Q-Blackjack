import random
import time

deck = {'HA': 11, 'SA': 11, 'CA': 11, 'DA': 11, 'H2': 2, 'S2': 2, 'C2': 2, 'D2': 2, 'H3': 3, 'S3': 3, 'C3': 3, 'D3': 3, 'H4': 4, 'S4': 4, 'C4': 4, 'D4': 4, 'H5': 5, 'S5': 5, 'C5': 5, 'D5': 5, 'H6': 6, 'S6': 6, 'C6': 6, 'D6': 6, 'H7': 7, 'S7': 7, 'C7': 7, 'D7': 7, 'H8': 8, 'S8': 8, 'C8': 8, 'D8': 8, 'H9': 9, 'S9': 9, 'C9': 9, 'D9': 9, 'H10': 10, 'S10': 10, 'C10': 10, 'D10': 10, 'HJ': 10, 'SJ': 10, 'CJ': 10, 'DJ': 10, 'HQ': 10, 'SQ': 10, 'CQ': 10, 'DQ': 10, 'HK': 10, 'SK': 10, 'CK': 10, 'DK': 10}


def deal():
    myHand = []
    dealerHand = []
    currentDeck = {'HA': 11, 'SA': 11, 'CA': 11, 'DA': 11, 'H2': 2, 'S2': 2, 'C2': 2, 'D2': 2, 'H3': 3, 'S3': 3, 'C3': 3, 'D3': 3, 'H4': 4, 'S4': 4, 'C4': 4, 'D4': 4, 'H5': 5, 'S5': 5, 'C5': 5, 'D5': 5, 'H6': 6, 'S6': 6, 'C6': 6, 'D6': 6, 'H7': 7, 'S7': 7, 'C7': 7, 'D7': 7, 'H8': 8, 'S8': 8, 'C8': 8, 'D8': 8, 'H9': 9, 'S9': 9, 'C9': 9, 'D9': 9, 'H10': 10, 'S10': 10, 'C10': 10, 'D10': 10, 'HJ': 10, 'SJ': 10, 'CJ': 10, 'DJ': 10, 'HQ': 10, 'SQ': 10, 'CQ': 10, 'DQ': 10, 'HK': 10, 'SK': 10, 'CK': 10, 'DK': 10}

    myHand.append(random.choice(list(currentDeck)))
    currentDeck.pop(myHand[0], None)
    dealerHand.append(random.choice(list(currentDeck)))
    currentDeck.pop(dealerHand[0], None)
    myHand.append(random.choice(list(currentDeck)))
    currentDeck.pop(myHand[1], None)
    dealerHand.append(random.choice(list(currentDeck)))
    currentDeck.pop(dealerHand[1], None)

    return myHand, dealerHand, currentDeck


def statePrint(state):
    print("_____________________________________")
    if not state:
        print("Dealer's Hand: ")
        for i in range(len(dealerHand)):
            print(dealerHand[i])
        print("Dealer's Count: ", countDealer)
    else:
        print("Dealer's Hand: ")
        print("X")
        print(dealerHand[1])
        print("Dealer's Count: ", countDealer)
    print("-----------")
    print("Your Hand:")
    for i in range(len(myHand)):
        print(myHand[i])
    print("Your Count: ", countPlayer)
    print("-----------")
    print("Bet: ", bet)
    print("\nYour Cash: ", cash)
    print("_____________________________________")
    return None


def isBj(hand):
    if 'A' in hand[1]:
        if 'J' in hand[0] or 'Q' in hand[0] or 'K' in hand[0] or '10' in hand[0]:
            return True
        else:
            return False
    elif 'J' in hand[1] or 'Q' in hand[1] or 'K' in hand[1] or '10' in hand[1]:
        if 'A' in hand[0]:
            return True
        else:
            return False


def transaction(endstate, bet, playersamount):
    if endstate == 1:
        print('You Win')
        playersamount = playersamount + (bet * 2)
    elif endstate == 3:
        print('Push')
        playersamount = playersamount + bet
    elif endstate == 2:
        print('You Lost')
    print('Your Cash: ', playersamount)
    return playersamount


def hit(currentDeck, hand, count):
    hand.append(random.choice(list(currentDeck)))
    currentDeck.pop(hand[-1], None)
    count = count + deck[hand[-1]]
    return currentDeck, hand, count


def aceCount(hand, count, alist):
    for ace in alist:
        if ace in hand:
            count = count - 10
            alist.remove(ace)
    return count, alist


cash = 1000

while cash > 0:
    hidden = True
    over = 0
    aceList = ['HA', 'CA', 'DA', 'SA']
    print('\nYour Cash: ', cash)
    print('How much do you want to bet?')
    bet = int(input())
    while not isinstance(bet, int):
        print("Please give a whole number")
        bet = int(input())
    while bet > cash:
        print("You are too broke for that amount")
        bet = int(input())
    cash = cash - bet

    myHand, dealerHand, currentDeck = deal()
    countDealer = deck[dealerHand[1]]
    countPlayer = deck[myHand[0]] + deck[myHand[1]]

    time.sleep(1)

    statePrint(hidden)

    time.sleep(2)

    if isBj(dealerHand):
        if isBj(myHand):
            over = 3
        else:
            over = 2
    elif isBj(myHand):
        over = 1

    if over != 0:
        cash = transaction(over, bet, cash)
        break

    print("\nType 'h' for hit, 's' for stand, 'd' for double")
    action = input()
    if action != 'h' and action != 's' and action != 'd':
        print("Not good, 'h' for hit, 's' for stand, 'd' for double please")
        action = input()
    if action == 'd':
        if cash >= bet:
            cash = cash - bet
            bet = bet * 2
            currentDeck, myHand, countPlayer = hit(currentDeck, myHand, countPlayer)
            if countPlayer > 21:
                countPlayer = aceCount(myHand, countPlayer)
            statePrint(hidden)
            time.sleep(2)
            print("\nType 'h' for hit, 's' for stand")
            action = input()
            if action != 'h' and action != 's':
                print("Not good, 'h' for hit, 's' for stand please")
                action = input()
        else:
            print("Not enough money!")
            time.sleep(2)
            print("\nType 'h' for hit, 's' for stand")
            action = input()
            if action != 'h' and action != 's':
                print("Not good, 'h' for hit, 's' for stand please")
                action = input()
    while action == 'h':
        currentDeck, myHand, countPlayer = hit(currentDeck, myHand, countPlayer)
        if countPlayer > 21:
            countPlayer, aceList = aceCount(myHand, countPlayer, aceList)
        statePrint(hidden)
        if countPlayer > 21:
            statePrint(hidden)
            print("Bust!")
            time.sleep(2)
            over = 2
            break
        print("\nType 'h' for hit, 's' for stand")
        action = input()
        if action != 'h' and action != 's':
            print("Not good, 'h' for hit, 's' for stand please")
            action = input()
    hidden = False
    countDealer = deck[dealerHand[0]] + deck[dealerHand[1]]
    statePrint(hidden)
    if over != 0:
        cash = transaction(over, bet, cash)
    else:
        while countDealer < 17 and countDealer < countPlayer:
            currentDeck, dealerHand, countDealer = hit(currentDeck, dealerHand, countDealer)
            if countDealer > 21:
                countDealer, aceList = aceCount(dealerHand, countDealer, aceList)
            statePrint(hidden)
            time.sleep(2)
        if countDealer == countPlayer:
            over = 3
        elif countDealer > 21:
            print("Bust!")
            over = 1
        elif countDealer < countPlayer:
            over = 1
        elif countDealer > countPlayer:
            over = 2
        if over != 0:
            cash = transaction(over, bet, cash)
        time.sleep(2)

if cash == 0:
    print("You're broke, get the hell out of my casino!")

# To-add: split
