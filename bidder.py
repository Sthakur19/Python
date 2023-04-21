from replit import clear
#HINT: You can call clear() to clear the output in the console.

from art import logo
print(logo)

bids = {}
biding_finish = False

def find_highest_bidder(biding_record):
  highest_bid = 0
  for bidder in biding_record:
    bid_amount = biding_record[bidder]
    if bid_amount > highest_bid:
      highest_bid = bid_amount
      winner = bidder
  print(f"The Winner is {winner} with the bid of ${highest_bid}")
  

while not biding_finish:
  name = input("What is your name ?")
  price = int(input("What is your bid ? $"))
  bids[name] = price
  should_continue = input("Are they any other bidder? Type 'Yes' or 'No'")
  if should_continue == 'no':
    biding_finish = True
    find_highest_bidder(bids)
  elif should_continue == 'Yes':
    clear()
    