TICKET_PRICE = 21

ticker_remaining = 100

# 

print("There are {} tickers reaming".format(ticker_remaining))

# Gather the user's name and assign it to a new variable
name = input("What is your name? ")

# Prompt the user by name and ask how many tickets they would like
num_tickets = input("How many tickets would you like, {}? ".format(name))
num_tickets = int(num_tickets)
# Calculate the price (number of ticker multipled by price) and assign it a variable
amount_due = num_tickets * TICKET_PRICE
# Output the price screen
print("The total due is €{}".format(amount_due))