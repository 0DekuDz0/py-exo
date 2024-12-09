name = input("What is your name? ")
if(name != "VIP"):
    numberOfTickets = int(input("How many tickets do you want? "))
    print("the total cost is", numberOfTickets * 15.50, "euros.")
else:
    print("You are a VIP, you get a free ticket")