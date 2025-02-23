import art
from replit import clear
#HINT: You can call clear() to clear the output in the console.
print(art.logo)
bids= {}
bidding_finished = False
def find_highest_bidder(bidding_record):
  highest_bid = 0
  winner = ""
  for bidder in bidding_record:
    if bidding_record[bidder] > highest_bid:
      highest_bid = bidding_record[bidder]
      winner = bidder
  print(f"The winner is {winner} with a bid of ${highest_bid}")
while not bidding_finished:
  name = input("What is your name?: ")
  price = int(input("What is your bid: $"))
  bids[name] = price
  should_continue = input("Are there any other bidders? Type 'yes or 'no'.\n")
  if should_continue == 'no':
    bidding_finished == True
    find_highest_bidder(bids)
    exit()
  elif should_continue == 'yes':
    clear()