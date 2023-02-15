from art import logo
import os
print(logo)

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

bids = {}
bidding_finished = False

def find_highest_bidder(bidding_record):
    highest_bid = 0
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")


while not bidding_finished:
    bidder_name = input("What is your name?: ")
    bidder_price = int(input("What is your Bid Price?: $"))
    bids[bidder_name] = bidder_price
    more_bidders = input("Are there more bidders? 'yes' or 'no'?\n")
    if more_bidders == "no":
        bidding_finished = True
        find_highest_bidder(bids)
    elif more_bidders == "yes":
        cls()
