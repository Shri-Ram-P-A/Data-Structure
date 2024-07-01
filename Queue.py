class TicketBooking:
    def __init__(self,limit):
        self.l = []
        self.limit = limit
    def book(self,name):
        if len(self.l) < self.limit:
            self.l.append(name)
        else:
            print("There is No available number of Tickets")

    def leave(self):
        if self.l is None:
            print("There is No One in Booking")
        else:
            print("Person leaved",self.l.pop(0))

    def booked(self):
        print("Number of persons booked :",len(self.l))

    def No_One(self):
        if(len(self.l) != 0):
            print("There is someone")
        else:
            print("No one in booked list")

    def List_Booking(self):
        for i in self.l:
            print(i)

ticketBooking = TicketBooking(5)
while True:
    a = input()
    if a=='1':
        ticketBooking.book(input())
    elif a=='2':
        ticketBooking.leave()
    elif a=='3':
        ticketBooking.booked()
    elif a=='4':
        ticketBooking.No_One()
    elif a=='5':
        ticketBooking.List_Booking()
    else:
        print("Tata ____ Bye")
        exit()