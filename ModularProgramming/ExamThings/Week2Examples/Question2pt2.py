 ## question 2 
def ticket_Amount():
    ticket_price = 5.50
    sold_by = ["Ann","Ben","Cal","Dan"]
    sold = [60,20,45,15]

    total_ticketsS = sum(sold)
    money_raised = total_ticketsS * ticket_price
    
    return money_raised , sold_by , sold

def moreThen40(sold_by, sold):
    cinema_tickets_recipients = []
    for idx, seller in enumerate(sold_by):
        if sold[idx] > 40:
            cinema_tickets_recipients.append(seller)
    return cinema_tickets_recipients


def main():
    money_raised, sold_by, sold = ticket_Amount()
    print("Raffle Ticket Sales")
    print("--------------------")
    print(f"A total of {sum(sold)} tickets were sold and €{money_raised:.2f} was raised.")
    
    cinema_ticket_recipients = moreThen40(sold_by, sold)
    if cinema_ticket_recipients:
        print(f"{len(cinema_ticket_recipients)} cinema ticket(s) will be awarded to:")
        for recipient in cinema_ticket_recipients:
            print(recipient)
    else:
        print("No one sold more than 40 tickets.")
    
main()

