TICKET_PRICE = 21

ticket_remaining = 100

while ticket_remaining >= 1:
    # 

    print("There are {} tickets reaming".format(ticket_remaining))

    # Gather the user's name and assign it to a new variable
    name = input("What is your name? ")

    # Prompt the user by name and ask how many tickets they would like
    num_tickets = input("How many tickets would you like, {}? ".format(name))
    num_tickets = int(num_tickets)
    # Calculate the price (number of ticker multipled by price) and assign it a variable
    amount_due = num_tickets * TICKET_PRICE
    # Output the price screen
    print("The total due is €{}".format(amount_due))

    # Prompt user
    should_proceed = input("Do you want proceed? Y/N")

    # If they want proceed Y/N
    if should_proceed.lower() == "y":
        
    # print out screen "SOLD!"
        print("SOLD!")
    # and them decrement the tickets remaining by number of ticket purchased
        ticket_remaining -= num_tickets
    # Otherwise...
   
   # Thank them by name
print("Sorry the tickets all sold out :(  "  )